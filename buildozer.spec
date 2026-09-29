[app]

# Application Title & Package
title = Jarvis AI
package.name = jarvisapp
package.domain = org.prince

# Source Code
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Version
version = 0.1

# Requirements
requirements = python3,kivy

# Orientation
orientation = portrait
fullscreen = 0

# Android Target Configurations
android.api = 33
android.minapi = 24
android.ndk = 25b

# Accept SDK Licenses Automatically
android.accept_sdk_license = True

# Target Architecture
android.archs = arm64-v8a

[buildozer]

# Log level 1 prevents log buffer overflow
log_level = 1
warn_on_root = 1
