%define name	4stAttack
%define version	2.1.4
%define release:	12

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
%{make_session}

%postun
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




%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.4-10mdv2011.0
+ Revision: 616405
- the mass rebuild of 2010.0 packages

* Mon Jun 08 2009 Jérôme Brenier <incubusss@mandriva.org> 2.1.4-9mdv2010.0
+ Revision: 384132
- drop old menu
- fix license
- clean spec file

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 2.1.4-8mdv2009.0
+ Revision: 218433
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
- %{update_menus} must be done in %%post, not %%postun (!)


* Fri Mar 16 2007 Claudio Matsuoka <claudio@mandriva.com> 2.1.4-8mdv2007.1
+ Revision: 145197
- Forced upgrade to test bugzilla product update.
- Import 4stAttack

* Mon Sep 04 2006 Nicolas L�cureuil <neoclust@mandriva.org> 2.1.4-7mdv2007.0
- XDG

* Mon Jan 02 2006 Lenny Cartier <lenny@mandrakesoft.com> 2.1.4-6mdk
- rebuild

* Thu Jun 10 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.1.4-5mdk
- rebuild

