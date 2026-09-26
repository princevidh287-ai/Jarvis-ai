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

# Requirements (Clean & Minimal)
requirements = python3,kivy

# Orientation
orientation = portrait
fullscreen = 0

# Android Target Configurations
android.api = 33
android.minapi = 21
android.ndk = 25b

# Stable P4A Release (Tested & Stable)
p4a.branch = v2024.01.21

# Accept Licenses
android.accept_sdk_license = True

# Sirf Single Architecture (Aapke phone ke liye fast aur error-free build)
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
