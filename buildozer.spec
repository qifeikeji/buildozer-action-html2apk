[app]
title = Localhost HTML App
package.name = localhostapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html
version = 1.0
requirements = python3,kivy
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.build_tools = 36.0.0

[buildozer]
android.accept_sdk_license = True
android.ndk = 25.2.9519653
android.sdk = 33
android.skip_update = False
log_level = 2
