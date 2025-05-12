[app]
title = Localhost HTML App
package.name = localhostapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html
version = 1.0
requirements = python3,kivy
android.permissions = INTERNET
android.api = 30
android.minapi = 21
android.build_tools = 30.0.3

[buildozer]
android.accept_sdk_license = True
android.ndk = 23.1.7779620
android.sdk = 30
android.skip_update = False
log_level = 2
