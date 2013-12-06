# revision 29803
# category Package
# catalog-ctan /fonts/stix
# catalog-date 2011-12-20 12:56:09 +0100
# catalog-license ofl
# catalog-version 1.0
Name:		texlive-stix
Version:	1.0
Release:	6
Summary:	OpenType Unicode maths fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/stix
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stix.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stix.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The STIX fonts are a suite of unicode OpenType fonts containing
a complete set of mathematical glyphs. The CTAN copy is a
mirror of their official release, organised as specified by the
TeX Directory Structure, for inclusion in standard TeX
distributions.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/opentype/public/stix/STIXGeneral.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXGeneralBol.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXGeneralBolIta.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXGeneralItalic.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXIntDBol.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXIntDReg.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXIntSmBol.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXIntSmReg.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXIntUpBol.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXIntUpDBol.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXIntUpDReg.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXIntUpReg.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXIntUpSmBol.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXIntUpSmReg.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXNonUni.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXNonUniBol.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXNonUniBolIta.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXNonUniIta.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXSizFiveSymReg.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXSizFourSymBol.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXSizFourSymReg.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXSizOneSymBol.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXSizOneSymReg.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXSizThreeSymBol.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXSizThreeSymReg.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXSizTwoSymBol.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXSizTwoSymReg.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXVar.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXVarBol.otf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXGeneral.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXGeneralBol.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXGeneralBolIta.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXGeneralItalic.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXIntDBol.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXIntDReg.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXIntSmBol.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXIntSmReg.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXIntUpBol.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXIntUpDBol.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXIntUpDReg.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXIntUpReg.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXIntUpSmBol.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXIntUpSmReg.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXNonUni.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXNonUniBol.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXNonUniBolIta.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXNonUniIta.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXSizFiveSymReg.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXSizFourSymBol.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXSizFourSymReg.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXSizOneSymBol.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXSizOneSymReg.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXSizThreeSymBol.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXSizThreeSymReg.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXSizTwoSymBol.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXSizTwoSymReg.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXVar.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/Glyphs/STIXVarBol.otf.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/README
%doc %{_texmfdistdir}/doc/fonts/stix/README.TEXLIVE
%doc %{_texmfdistdir}/doc/fonts/stix/STIX_Font_License_2010.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
