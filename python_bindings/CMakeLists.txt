##
# Load Python dependencies, including external pybind11
##

find_package(Python3 REQUIRED COMPONENTS Interpreter Development)

set(PYBIND11_VER 2.10.2)
find_package(pybind11 ${PYBIND11_VER} QUIET)
if (NOT pybind11_FOUND)
    include(FetchContent)
    FetchContent_Declare(pybind11
                         GIT_REPOSITORY https://github.com/pybind/pybind11.git
                         GIT_TAG v${PYBIND11_VER})
    FetchContent_MakeAvailable(pybind11)
endif ()

##
# Add our sources to this sub-tree.
##

add_subdirectory(src)
