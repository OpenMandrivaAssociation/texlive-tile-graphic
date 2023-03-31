Name:		texlive-tile-graphic
Version:	55325
Release:	2
Summary:	Create tiles of a graphical file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tile-graphic
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tile-graphic.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tile-graphic.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tile-graphic.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package breaks a given graphical file into n rows and m
columns of subgraphics, which are called tiles. The tiles can
be written separately to individual PDF files, or packaged into
a single PDF file.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/tile-graphic
%{_texmfdistdir}/tex/latex/tile-graphic
%doc %{_texmfdistdir}/doc/latex/tile-graphic

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
