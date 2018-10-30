Name:		texlive-stix
Version:	1.1.3
Release:	3
Summary:	OpenType Unicode maths fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/stix
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stix.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stix.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stix.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The STIX fonts are a suite of unicode OpenType fonts containing
a complete set of mathematical glyphs. The CTAN package is a
copy of the fonts' official release, organised as specified by
the TeX Directory Structure, for inclusion in standard TeX
distributions. A Type 1 only distribution of the fonts is
available in the esstix bundle.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/stix
%{_texmfdistdir}/fonts/map/dvips/stix
%{_texmfdistdir}/fonts/opentype/public/stix
%{_texmfdistdir}/fonts/source/public/stix
%{_texmfdistdir}/fonts/tfm/public/stix
%{_texmfdistdir}/fonts/type1/public/stix
%{_texmfdistdir}/fonts/vf/public/stix
%{_texmfdistdir}/tex/latex/stix
%doc %{_texmfdistdir}/doc/fonts/stix
#- source
%doc %{_texmfdistdir}/source/latex/stix

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
