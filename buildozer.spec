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
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Custom source code for requirements
# p4a.branch = master लाइन को अनलॉक किया गया है
p4a.branch = master

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version to use
# android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (list) List of Java .jar files to add to the libs
# android.add_jars = foo.jar,bar.jar

# (list) List of Java files to add to the project
# android.add_src =

# (list) Android AAR archives to add
# android.add_aars =

# (list) Gradle dependencies
# android.gradle_dependencies =

# (bool) Enable AndroidX support
android.androidx = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (1 = display, 0 = hide)
warn_on_root = 1

