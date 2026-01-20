[app]
title = YAY-on-pocket
package.name = yaylinux
package.domain = com.hyu
source.dir = app
source.include_exts = py,png,jpg,kv,txt
version = 0.1
requirements = python3,kivy,pyjnius
orientation = portrait
android.api = 33
android.minapi = 21
android.add_src = src
android.gradle_dependencies = implementation 'androidx.security:security-crypto:1.1.0'
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
