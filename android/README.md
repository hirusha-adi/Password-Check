# Android App

<div align="center">
  <img src="https://raw.githubusercontent.com/hirusha-adi/is-it-healthy/main/artwork/github/Android_logo_2019_(stacked).svg.png" width="250">
</div>

This is an Android Wrapper application to create native Android Apps from an offline-capable Progressive Web App, cloned from [xtools-at/Android-PWA-Wrapper](https://github.com/xtools-at/Android-PWA-Wrapper) and changed to match this applications need accordingly

## Capabilities

- Sets up a WebView just the way PWAs/SPAs like it (e.g. enables App cache and DOM storage, ...).
- Shows a loading spinner while loading the Web App.
- Opens all external URLs in the device's Browser instead.
- Is compatible down to JellyBean, although it's recommended to build for SDK Version >= 19 (KitKat). Building for SDK Version >= 21 (Lollipop) puts you on the safe side without having to worry too much about Browser support.
- APK-size < 1.4 MB. The latest cat video from WhatsApp weighs heavier ;)

## Customizations

- Get Android Studio 3.4+
- Put your Web App's URL in _WEBAPP_URL_ in `app\src\main\java\at\xtools\pwawrapper\Constants.java`
- Replace _app_name_ in `app\src\main\res\values\strings.xml` with the name of your App
- Add your own primary colors to `app\src\main\res\values\colors.xml` (_colorPrimary, colorPrimaryDark, colorPrimaryLight_)
- Change the package name in `app\build.gradle`, _applicationId_
- Build App in Android Studio

## Build Guide

- Copy either the `index.dark.html` or the `index.light.html` into `app\src\main\assets\index.html`
- Open the the current working directory in Adnroid Studio
- Change the app name in `app\src\main\res\values\strings.xml` in _line 2_
- Uncomment the color mode that you are using and comment the one that you do not in `app\src\main\res\values\colors.xml`. Line 4-9 is for light mode and Line 12-17 is for dark mode
- Build APK in Android Studio

Main Repository: [xtools-at/Android-PWA-Wrapper](https://github.com/xtools-at/Android-PWA-Wrapper)
