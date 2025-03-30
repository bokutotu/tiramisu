FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    cmake \
    ninja-build \
    build-essential \
    wget \
    ca-certificates \
    autoconf \
    libtool \
    pkg-config \
    zlib1g-dev \
    libpng-dev \
    libedit-dev \
    libncurses5-dev \
    python3 \
    python3-dev \
    coreutils \
    && \
    rm -rf /var/lib/apt/lists/*

ENV TIRAMISU_ROOT=/opt/tiramisu
WORKDIR ${TIRAMISU_ROOT}

COPY . ${TIRAMISU_ROOT}

RUN git submodule update --init --recursive

RUN cd ${TIRAMISU_ROOT}/3rdParty/llvm && \
    mkdir -p build prefix && \
    cd build && \
    cmake -G Ninja \
          -S ../llvm \
          -DHAVE_LIBEDIT=0 \
          -DLLVM_ENABLE_TERMINFO=OFF \
          -DLLVM_ENABLE_PROJECTS='clang;lld;clang-tools-extra' \
          -DLLVM_ENABLE_EH=ON \
          -DLLVM_ENABLE_RTTI=ON \
          -DLLVM_BUILD_32_BITS=OFF \
          -DLLVM_TARGETS_TO_BUILD='X86;ARM;AArch64;Mips;NVPTX;PowerPC' \
          -DLLVM_ENABLE_ASSERTIONS=ON \
          -DCMAKE_BUILD_TYPE=Release \
          -DCMAKE_INSTALL_PREFIX=${TIRAMISU_ROOT}/3rdParty/llvm/prefix \
          -DCMAKE_MAKE_PROGRAM='ninja' \
          -DCMAKE_C_COMPILER='gcc' \
          -DCMAKE_CXX_COMPILER='g++' \
          && \
    cmake --build . -j $(nproc --all) && \
    cmake --install .

RUN cd ${TIRAMISU_ROOT}/3rdParty/isl && \
    mkdir -p build && \
    touch aclocal.m4 Makefile.am Makefile.in || true && \
    ./configure --prefix=${TIRAMISU_ROOT}/3rdParty/isl/build --with-int=imath && \
    make -j $(nproc --all) && \
    make install

RUN cd ${TIRAMISU_ROOT}/3rdParty/Halide && \
    mkdir -p build install && \
    cmake -G Ninja \
          -S . \
          -B build \
          -DCMAKE_BUILD_TYPE=Release \
          -DLLVM_DIR=${TIRAMISU_ROOT}/3rdParty/llvm/prefix/lib/cmake/llvm \
          -DCMAKE_MAKE_PROGRAM='ninja' \
          -DCMAKE_C_COMPILER='gcc' \
          -DCMAKE_CXX_COMPILER='g++' \
          -DCMAKE_CXX_FLAGS='-std=c++17' \
          -DCMAKE_INSTALL_PREFIX=${TIRAMISU_ROOT}/3rdParty/Halide/install \
          -DHALIDE_NO_JPEG=ON \
          -DHALIDE_NO_PNG=ON \
          && \
    cmake --build build -j $(nproc --all) && \
    cmake --install build

ENV PATH=${TIRAMISU_ROOT}/3rdParty/llvm/prefix/bin:${PATH}
ENV LD_LIBRARY_PATH=${TIRAMISU_ROOT}/3rdParty/isl/build/lib:${TIRAMISU_ROOT}/3rdParty/llvm/prefix/lib:${TIRAMISU_ROOT}/3rdParty/Halide/install/lib:${LD_LIBRARY_PATH:-}
ENV CMAKE_PREFIX_PATH=${TIRAMISU_ROOT}/3rdParty/isl/build:${TIRAMISU_ROOT}/3rdParty/llvm/prefix:${TIRAMISU_ROOT}/3rdParty/Halide/install:${CMAKE_PREFIX_PATH:-}

WORKDIR ${TIRAMISU_ROOT}
RUN mkdir build

RUN cmake . -B build -GNinja \
    -DISL_INCLUDE_DIRECTORY=${TIRAMISU_ROOT}/3rdParty/isl/include \
    -DISL_LIB_DIRECTORY=${TIRAMISU_ROOT}/3rdParty/isl/build/lib \
    -DWITH_PYTHON_BINDINGS=FALSE

# Tiramisu をビルド (変更なし)
RUN cmake --build build -j $(nproc --all)

CMD ["bash"]
