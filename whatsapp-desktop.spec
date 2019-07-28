
%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress

Summary:   WhatsApp Desktop
Name:      WhatsApp
Release:   1
License:   GPL
Group:     None
BuildArchitectures: x86_64
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Source:    dummy.tar.bz2
Requires:  libXScrnSaver
Provides:  libffmpeg.so()(64bit)

%description
Unofficial WhatsApp desktop client, based on the official WhatsApp web app. Built with Electron.

%prep
%setup -c -q -T -D -a 0

%build
# Empty section.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
mkdir -p %{buildroot}/usr/share/applications/
mkdir -p %{buildroot}/usr/share/metainfo/
mkdir -p %{buildroot}/usr/share/icons/hicolor/128x128/apps/
mkdir -p %{buildroot}/usr/share/icons/hicolor/64x64/apps/
cp "%{_topdir}/../app/assets/icon/icon@2x.png" %{buildroot}/usr/share/icons/hicolor/128x128/apps/whatsapp.png
cp "%{_topdir}/../app/assets/icon/icon.png" %{buildroot}/usr/share/icons/hicolor/64x64/apps/whatsapp.png
cp %{_topdir}/../whatsappdesktop.desktop %{buildroot}/usr/share/applications/
# copy files in builddir
install -d -m 0755 %{buildroot}/opt/whatsapp-desktop/
install -d -m 0755 %{buildroot}/%{_bindir}
cp -ar %{_topdir}/../dist/WhatsApp-linux-x64/* %{buildroot}/opt/whatsapp-desktop/
ln -sf /opt/whatsapp-desktop/WhatsApp %{buildroot}/%{_bindir}/WhatsApp

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
/opt/whatsapp-desktop/*
%{_bindir}/WhatsApp
/usr/share/applications/whatsappdesktop.desktop
/usr/share/icons/hicolor/128x128/apps/whatsapp.png
/usr/share/icons/hicolor/64x64/apps/whatsapp.png
