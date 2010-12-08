%define name	4stAttack
%define version	2.1.4
%define release	%mkrel 10

Summary:	Connect-four for pygame
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Games/Boards
License:	GPLv2
URL:		http://forcedattack.sourceforge.net
Source:		http://belnet.dl.sourceforge.net/sourceforge/forcedattack/%{name}-%{version}.tar.bz2
Source2:	%{name}-icons.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	pygame >= 1.5.3
BuildArch:	noarch

%description
4stAttack is a game in which you have to try to out-smart your opponent.
The goal of the game is to connect four of stones in  a	 straight  line.
This can be horizontaly, vertically or diagonally.

This rpm works with the portable pygame game-engine.


%prep
%setup -q
%setup -q -T -D -a2

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_gamesbindir}/%{name}
cp -R *  %{buildroot}%{_gamesbindir}/%{name}
#icon
install -D -m644 %{name}48.png %{buildroot}%{_liconsdir}/%{name}.png
install -D -m644 %{name}32.png %{buildroot}%{_iconsdir}/%{name}.png
install -D -m644 %{name}16.png %{buildroot}%{_miconsdir}/%{name}.png

# Lets make a wrapper.
mkdir -p %{buildroot}%{_bindir}
cat << EOF > %{buildroot}%{_bindir}/%{name}
#!/bin/sh
cd %{_prefix}/games/%{name}

if [ ! -f ~/.%{name} ]; then
    cp settings.ini ~/.%{name} || exit 1
fi

%{__python} 4stattack.py -ini ~/.%{name}
EOF

# Menu entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=Connect-four for pygame
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Games-Boards;Game;BoardGame;
EOF


%post
%if %mdkversion < 200900
%{update_menus}
%endif
%{make_session}

%postun
%if %mdkversion < 200900
%{clean_menus}
%endif
%{make_session}

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc changelog.txt README.txt
%dir %{_gamesbindir}/%{name}
%{_gamesbindir}/%{name}/*

%{_datadir}/applications/mandriva-%{name}.desktop

%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png

%defattr(755,root,root,755)
%{_bindir}/%{name}


