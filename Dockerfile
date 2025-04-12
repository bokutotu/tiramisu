FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    git \
    cmake \
    ninja-build \
    build-essential \
    autoconf \
    libtool \
    wget \
    python3 \
    python3-dev \
    mpi-default-dev \
    openssh-client \
    llvm-14-dev \
    libclang-14-dev \
    liblld-14-dev \
    clang-14 \
    libisl-dev \
    libpng-dev \
    libjpeg-turbo8-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /tiramisu

COPY . .

RUN git submodule update --init --recursive

ARG LLVM_DIR=/usr/lib/llvm-14/lib/cmake/llvm

RUN cd 3rdParty/Halide && \
    rm -rf build && \ 
    cmake -G Ninja \
          -DCMAKE_BUILD_TYPE=Release \
          -DLLVM_DIR=${LLVM_DIR} \
          -DHalide_SHARED_LLVM=YES \
          -DTARGET_WEBASSEMBLY=OFF \
          -S . -B build && \
    cmake --build build -j$(nproc) && \
    cmake --install build

RUN cd 3rdParty/isl && \
    touch aclocal.m4 Makefile.am Makefile.in && \
    ./configure --prefix=$PWD/build/ --with-int=imath && \
    make -j$(nproc) && \
    make install

RUN mkdir build && \
    cd build && \
    cmake .. \
        -G Ninja \
        -DCMAKE_C_COMPILER=/usr/bin/clang-14 \
        -DCMAKE_CXX_COMPILER=/usr/bin/clang++-14 \
    && \
    cmake --build . -j $(nproc)

CMD ["bash"]
