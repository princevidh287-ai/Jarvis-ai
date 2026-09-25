[app]

# (str) Title of your application
title = Jarvis AI

# (str) Package name
package.name = jarvisapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.prince

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Custom source code for requirements
p4a.branch = master

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Target Android API
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (bool) Accept Android SDK licenses
android.accept_sdk_license = True

# (bool) Enable AndroidX support
android.androidx = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
