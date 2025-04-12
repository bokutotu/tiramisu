cmake_minimum_required(VERSION 3.10)
project(BlurExample CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(TIRAMISU_SOURCE_DIR /tiramisu)
set(TIRAMISU_BUILD_DIR /tiramisu/build)
set(TIRAMISU_INCLUDE_DIR ${TIRAMISU_SOURCE_DIR}/include)
set(TIRAMISU_3RDPARTY_DIR ${TIRAMISU_SOURCE_DIR}/3rdParty)

include_directories(${TIRAMISU_INCLUDE_DIR})
include_directories(/usr/local/include) # Halide headers installed globally
include_directories(${TIRAMISU_3RDPARTY_DIR}/isl/build/include)

link_directories(${TIRAMISU_BUILD_DIR})
link_directories(/usr/local/lib) # Halide library installed globally
link_directories(${TIRAMISU_3RDPARTY_DIR}/isl/build/lib)

add_executable(blur blur.cpp)

target_link_libraries(blur PRIVATE tiramisu Halide isl)
