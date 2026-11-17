[app]

# (str) Title of your application
title = Osobine Broja

# (str) Package name
package.name = osobinebroja

# (str) Package domain (needed for android packaging)
package.domain = org.matematika

# (str) Source files where the *.py files are located
source.dir = .

# (list) Source files to include (let it include py files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Add Python modules that need to be packaged here
requirements = python3,kivy

# (str) Supported orientations (portrait, landscape or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# (list) architectures
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable backup
android.allow_backup = True

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.min_api = 24

# (str) Android NDK version to use (fiksirano na stabilnu verziju 25b)
android.ndk = 25b


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
