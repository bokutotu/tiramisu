# Use a recent Ubuntu LTS version as the base image
FROM ubuntu:22.04

# Avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install essential build tools and dependencies required by Tiramisu and its submodules build script
# Note: LLVM, Halide, and ISL will be built from source via the script using the copied source code
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    # Basic tools needed for build environment
    git \
    cmake \
    ninja-build \
    build-essential \
    wget \
    ca-certificates \
    # Tiramisu prerequisites mentioned in README
    autoconf \
    libtool \
    # Dependencies potentially needed for building LLVM/Clang/Halide from source
    pkg-config \
    zlib1g-dev \
    libedit-dev \
    libncurses5-dev \
    # Python is needed by some build scripts even if bindings are not used
    python3 \
    # # Optional: For Python bindings (choose python3 version as needed)
    # python3-pip \
    python3-dev \
    # cython3 \
    # python3-numpy \
    # Optional: For MPI support
    # libopenmpi-dev openssh-client \
    && \
    # Optional: Install Pybind11 for Python bindings (if needed)
    # pip3 install pybind11==2.10.4 \
    # Clean up apt cache
    rm -rf /var/lib/apt/lists/*

# Set the working directory within the container
ENV TIRAMISU_ROOT=/opt/tiramisu
WORKDIR ${TIRAMISU_ROOT}

# Copy the entire Tiramisu source directory (context) into the container
# Assumes Dockerfile is in the Tiramisu root directory on the host.
# Use .dockerignore to exclude unnecessary files/dirs (like .git, build/, etc.)
COPY . ${TIRAMISU_ROOT}

# Run the script to build submodules (ISL, LLVM, Halide) using the copied source
# This step can take a significant amount of time (potentially hours)
# Ensure host had submodules initialized/updated before building the Docker image
RUN ./utils/scripts/install_submodules.sh ${TIRAMISU_ROOT}

# Add the built Halide's CMake configuration path to CMAKE_PREFIX_PATH
# This helps CMake find the Halide built as a submodule
ENV CMAKE_PREFIX_PATH=${TIRAMISU_ROOT}/3rdParty/Halide/build/:${CMAKE_PREFIX_PATH}

# Create the build directory for Tiramisu itself
# Use RUN arguments to avoid permission issues if any occur with WORKDIR context
RUN mkdir build

# Configure Tiramisu using CMake
# It should now find Halide via CMAKE_PREFIX_PATH.
# ISL should also be found within 3rdParty, but specify paths if needed.
# Adjust CMake options based on your needs (GPU, MPI, Python bindings, Autoscheduler)
RUN cmake . -B build -GNinja \
    # Specify ISL paths built by the script if not found automatically
    # Check the actual paths inside 3rdParty/isl/ after the script runs
    -DISL_INCLUDE_DIRECTORY=${TIRAMISU_ROOT}/3rdParty/isl/include \
    -DISL_LIB_DIRECTORY=${TIRAMISU_ROOT}/3rdParty/isl/build/lib \
    # Example: Enable Python bindings if needed
    -DWITH_PYTHON_BINDINGS=FALSE \
    # -DPython3_EXECUTABLE=/usr/bin/python3 \
    # Add other options like -DUSE_GPU=TRUE or -DUSE_MPI=TRUE if needed

# Build Tiramisu
RUN cmake --build build

# --- Optional: Run tests ---
# WORKDIR ${TIRAMISU_ROOT}/build
# RUN ctest

# --- Optional: Installation ---
# If you want to install Tiramisu within the image:
# WORKDIR ${TIRAMISU_ROOT} # Go back to root if needed
# RUN cmake --install build --prefix /usr/local/tiramisu
# ENV PATH=/usr/local/tiramisu/bin:${PATH}
# ENV LD_LIBRARY_PATH=/usr/local/tiramisu/lib:${LD_LIBRARY_PATH}
# If Python bindings installed:
# ENV PYTHONPATH=/usr/local/tiramisu/python:${PYTHONPATH} # Adjust python path

# Set default command to bash for interactive use
CMD ["bash"]
