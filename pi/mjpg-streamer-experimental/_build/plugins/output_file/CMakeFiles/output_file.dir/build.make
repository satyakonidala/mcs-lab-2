# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.13

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/pi/mjpg-streamer/mjpg-streamer-experimental

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/pi/mjpg-streamer/mjpg-streamer-experimental/_build

# Include any dependencies generated for this target.
include plugins/output_file/CMakeFiles/output_file.dir/depend.make

# Include the progress variables for this target.
include plugins/output_file/CMakeFiles/output_file.dir/progress.make

# Include the compile flags for this target's objects.
include plugins/output_file/CMakeFiles/output_file.dir/flags.make

plugins/output_file/CMakeFiles/output_file.dir/output_file.c.o: plugins/output_file/CMakeFiles/output_file.dir/flags.make
plugins/output_file/CMakeFiles/output_file.dir/output_file.c.o: ../plugins/output_file/output_file.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/mjpg-streamer/mjpg-streamer-experimental/_build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object plugins/output_file/CMakeFiles/output_file.dir/output_file.c.o"
	cd /home/pi/mjpg-streamer/mjpg-streamer-experimental/_build/plugins/output_file && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/output_file.dir/output_file.c.o   -c /home/pi/mjpg-streamer/mjpg-streamer-experimental/plugins/output_file/output_file.c

plugins/output_file/CMakeFiles/output_file.dir/output_file.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/output_file.dir/output_file.c.i"
	cd /home/pi/mjpg-streamer/mjpg-streamer-experimental/_build/plugins/output_file && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/pi/mjpg-streamer/mjpg-streamer-experimental/plugins/output_file/output_file.c > CMakeFiles/output_file.dir/output_file.c.i

plugins/output_file/CMakeFiles/output_file.dir/output_file.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/output_file.dir/output_file.c.s"
	cd /home/pi/mjpg-streamer/mjpg-streamer-experimental/_build/plugins/output_file && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/pi/mjpg-streamer/mjpg-streamer-experimental/plugins/output_file/output_file.c -o CMakeFiles/output_file.dir/output_file.c.s

# Object files for target output_file
output_file_OBJECTS = \
"CMakeFiles/output_file.dir/output_file.c.o"

# External object files for target output_file
output_file_EXTERNAL_OBJECTS =

plugins/output_file/output_file.so: plugins/output_file/CMakeFiles/output_file.dir/output_file.c.o
plugins/output_file/output_file.so: plugins/output_file/CMakeFiles/output_file.dir/build.make
plugins/output_file/output_file.so: plugins/output_file/CMakeFiles/output_file.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/pi/mjpg-streamer/mjpg-streamer-experimental/_build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C shared library output_file.so"
	cd /home/pi/mjpg-streamer/mjpg-streamer-experimental/_build/plugins/output_file && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/output_file.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
plugins/output_file/CMakeFiles/output_file.dir/build: plugins/output_file/output_file.so

.PHONY : plugins/output_file/CMakeFiles/output_file.dir/build

plugins/output_file/CMakeFiles/output_file.dir/clean:
	cd /home/pi/mjpg-streamer/mjpg-streamer-experimental/_build/plugins/output_file && $(CMAKE_COMMAND) -P CMakeFiles/output_file.dir/cmake_clean.cmake
.PHONY : plugins/output_file/CMakeFiles/output_file.dir/clean

plugins/output_file/CMakeFiles/output_file.dir/depend:
	cd /home/pi/mjpg-streamer/mjpg-streamer-experimental/_build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pi/mjpg-streamer/mjpg-streamer-experimental /home/pi/mjpg-streamer/mjpg-streamer-experimental/plugins/output_file /home/pi/mjpg-streamer/mjpg-streamer-experimental/_build /home/pi/mjpg-streamer/mjpg-streamer-experimental/_build/plugins/output_file /home/pi/mjpg-streamer/mjpg-streamer-experimental/_build/plugins/output_file/CMakeFiles/output_file.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : plugins/output_file/CMakeFiles/output_file.dir/depend

