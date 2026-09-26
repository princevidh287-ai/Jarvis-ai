[app]

# Application Title
title = Jarvis AI

# Package Name & Domain
package.name = jarvisapp
package.domain = org.prince

# Source Code
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Application Version
version = 0.1

# Requirements
requirements = python3,kivy

# Supported Orientation & Fullscreen
orientation = portrait
fullscreen = 0

# Android API & NDK Configuration
android.api = 33
android.minapi = 21
android.ndk = 25b

# Accept SDK Licenses Automatically
android.accept_sdk_license = True

# Target Architectures
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

# Log Level
log_level = 2
warn_on_root = 1
