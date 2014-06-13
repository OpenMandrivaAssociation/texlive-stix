# revision 32585
# category Package
# catalog-ctan /fonts/stix
# catalog-date 2014-01-03 10:16:06 +0100
# catalog-license ofl
# catalog-version 2014-01-01
Name:		texlive-stix
Version:	20140101
Release:	2
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
%{_texmfdistdir}/fonts/enc/dvips/stix/stix-extra1.enc
%{_texmfdistdir}/fonts/enc/dvips/stix/stix-extra2.enc
%{_texmfdistdir}/fonts/enc/dvips/stix/stix-extra3.enc
%{_texmfdistdir}/fonts/enc/dvips/stix/stix-ot1.enc
%{_texmfdistdir}/fonts/enc/dvips/stix/stix-ot2.enc
%{_texmfdistdir}/fonts/enc/dvips/stix/stix-t1.enc
%{_texmfdistdir}/fonts/enc/dvips/stix/stix-ts1.enc
%{_texmfdistdir}/fonts/map/dvips/stix/stix.map
%{_texmfdistdir}/fonts/opentype/public/stix/STIX-Bold.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIX-BoldItalic.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIX-Italic.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIX-Regular.otf
%{_texmfdistdir}/fonts/opentype/public/stix/STIXMath-Regular.otf
%{_texmfdistdir}/fonts/source/public/stix/ot1-stixgeneral-bold.pl
%{_texmfdistdir}/fonts/source/public/stix/ot1-stixgeneral-bolditalic.pl
%{_texmfdistdir}/fonts/source/public/stix/ot1-stixgeneral-italic.pl
%{_texmfdistdir}/fonts/source/public/stix/ot1-stixgeneral.pl
%{_texmfdistdir}/fonts/source/public/stix/ot1-stixgeneralsc-bold.vpl
%{_texmfdistdir}/fonts/source/public/stix/ot1-stixgeneralsc.vpl
%{_texmfdistdir}/fonts/source/public/stix/ot2-stixgeneral-bold.pl
%{_texmfdistdir}/fonts/source/public/stix/ot2-stixgeneral-bolditalic.pl
%{_texmfdistdir}/fonts/source/public/stix/ot2-stixgeneral-italic.pl
%{_texmfdistdir}/fonts/source/public/stix/ot2-stixgeneral.pl
%{_texmfdistdir}/fonts/source/public/stix/ot2-stixgeneralsc-bold.vpl
%{_texmfdistdir}/fonts/source/public/stix/ot2-stixgeneralsc.vpl
%{_texmfdistdir}/fonts/source/public/stix/stix-extra1-bold.pl
%{_texmfdistdir}/fonts/source/public/stix/stix-extra1.pl
%{_texmfdistdir}/fonts/source/public/stix/stix-extra2-bold.pl
%{_texmfdistdir}/fonts/source/public/stix/stix-extra2.pl
%{_texmfdistdir}/fonts/source/public/stix/stix-extra3-bold.pl
%{_texmfdistdir}/fonts/source/public/stix/stix-extra3.pl
%{_texmfdistdir}/fonts/source/public/stix/stix-mathbb-bold.pl
%{_texmfdistdir}/fonts/source/public/stix/stix-mathbb.pl
%{_texmfdistdir}/fonts/source/public/stix/stix-mathbbit-bold.pl
%{_texmfdistdir}/fonts/source/public/stix/stix-mathbbit.pl
%{_texmfdistdir}/fonts/source/public/stix/stix-mathcal-bold.pl
%{_texmfdistdir}/fonts/source/public/stix/stix-mathcal.pl
%{_texmfdistdir}/fonts/source/public/stix/stix-mathex-bold.pl
%{_texmfdistdir}/fonts/source/public/stix/stix-mathex.pl
%{_texmfdistdir}/fonts/source/public/stix/stix-mathfrak-bold.pl
%{_texmfdistdir}/fonts/source/public/stix/stix-mathfrak.pl
%{_texmfdistdir}/fonts/source/public/stix/stix-mathit-bold.pl
%{_texmfdistdir}/fonts/source/public/stix/stix-mathit.pl
%{_texmfdistdir}/fonts/source/public/stix/stix-mathrm-bold.pl
%{_texmfdistdir}/fonts/source/public/stix/stix-mathrm.pl
%{_texmfdistdir}/fonts/source/public/stix/stix-mathscr-bold.pl
%{_texmfdistdir}/fonts/source/public/stix/stix-mathscr.pl
%{_texmfdistdir}/fonts/source/public/stix/stix-mathsf-bold.pl
%{_texmfdistdir}/fonts/source/public/stix/stix-mathsf.pl
%{_texmfdistdir}/fonts/source/public/stix/stix-mathsfit-bold.pl
%{_texmfdistdir}/fonts/source/public/stix/stix-mathsfit.pl
%{_texmfdistdir}/fonts/source/public/stix/stix-mathtt-bold.pl
%{_texmfdistdir}/fonts/source/public/stix/stix-mathtt.pl
%{_texmfdistdir}/fonts/source/public/stix/t1-stixgeneral-bold.pl
%{_texmfdistdir}/fonts/source/public/stix/t1-stixgeneral-bolditalic.pl
%{_texmfdistdir}/fonts/source/public/stix/t1-stixgeneral-italic.pl
%{_texmfdistdir}/fonts/source/public/stix/t1-stixgeneral.pl
%{_texmfdistdir}/fonts/source/public/stix/t1-stixgeneralsc-bold.vpl
%{_texmfdistdir}/fonts/source/public/stix/t1-stixgeneralsc.vpl
%{_texmfdistdir}/fonts/source/public/stix/ts1-stixgeneral-bold.pl
%{_texmfdistdir}/fonts/source/public/stix/ts1-stixgeneral-bolditalic.pl
%{_texmfdistdir}/fonts/source/public/stix/ts1-stixgeneral-italic.pl
%{_texmfdistdir}/fonts/source/public/stix/ts1-stixgeneral.pl
%{_texmfdistdir}/fonts/tfm/public/stix/ot1-stixgeneral-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/ot1-stixgeneral-bolditalic.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/ot1-stixgeneral-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/ot1-stixgeneral.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/ot1-stixgeneralsc-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/ot1-stixgeneralsc.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/ot2-stixgeneral-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/ot2-stixgeneral-bolditalic.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/ot2-stixgeneral-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/ot2-stixgeneral.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/ot2-stixgeneralsc-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/ot2-stixgeneralsc.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/stix-extra1.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/stix-extra2.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/stix-extra3.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/stix-mathbb-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/stix-mathbb.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/stix-mathbbit-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/stix-mathbbit.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/stix-mathcal-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/stix-mathcal.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/stix-mathex-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/stix-mathex.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/stix-mathfrak-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/stix-mathfrak.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/stix-mathit-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/stix-mathit.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/stix-mathrm-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/stix-mathrm.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/stix-mathscr-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/stix-mathscr.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/stix-mathsf-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/stix-mathsf.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/stix-mathsfit-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/stix-mathsfit.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/stix-mathtt-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/stix-mathtt.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/t1-stixgeneral-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/t1-stixgeneral-bolditalic.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/t1-stixgeneral-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/t1-stixgeneral.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/t1-stixgeneralsc-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/t1-stixgeneralsc.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/ts1-stixgeneral-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/ts1-stixgeneral-bolditalic.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/ts1-stixgeneral-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/stix/ts1-stixgeneral.tfm
%{_texmfdistdir}/fonts/type1/public/stix/STIXGeneral-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/stix/STIXGeneral-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/public/stix/STIXGeneral-Italic.pfb
%{_texmfdistdir}/fonts/type1/public/stix/STIXGeneral-Regular.pfb
%{_texmfdistdir}/fonts/type1/public/stix/stix-mathbb-bold.pfb
%{_texmfdistdir}/fonts/type1/public/stix/stix-mathbb.pfb
%{_texmfdistdir}/fonts/type1/public/stix/stix-mathbbit-bold.pfb
%{_texmfdistdir}/fonts/type1/public/stix/stix-mathbbit.pfb
%{_texmfdistdir}/fonts/type1/public/stix/stix-mathcal-bold.pfb
%{_texmfdistdir}/fonts/type1/public/stix/stix-mathcal.pfb
%{_texmfdistdir}/fonts/type1/public/stix/stix-mathex-bold.pfb
%{_texmfdistdir}/fonts/type1/public/stix/stix-mathex.pfb
%{_texmfdistdir}/fonts/type1/public/stix/stix-mathfrak-bold.pfb
%{_texmfdistdir}/fonts/type1/public/stix/stix-mathfrak.pfb
%{_texmfdistdir}/fonts/type1/public/stix/stix-mathit-bold.pfb
%{_texmfdistdir}/fonts/type1/public/stix/stix-mathit.pfb
%{_texmfdistdir}/fonts/type1/public/stix/stix-mathrm-bold.pfb
%{_texmfdistdir}/fonts/type1/public/stix/stix-mathrm.pfb
%{_texmfdistdir}/fonts/type1/public/stix/stix-mathscr-bold.pfb
%{_texmfdistdir}/fonts/type1/public/stix/stix-mathscr.pfb
%{_texmfdistdir}/fonts/type1/public/stix/stix-mathsf-bold.pfb
%{_texmfdistdir}/fonts/type1/public/stix/stix-mathsf.pfb
%{_texmfdistdir}/fonts/type1/public/stix/stix-mathsfit-bold.pfb
%{_texmfdistdir}/fonts/type1/public/stix/stix-mathsfit.pfb
%{_texmfdistdir}/fonts/type1/public/stix/stix-mathtt-bold.pfb
%{_texmfdistdir}/fonts/type1/public/stix/stix-mathtt.pfb
%{_texmfdistdir}/fonts/vf/public/stix/ot1-stixgeneralsc-bold.vf
%{_texmfdistdir}/fonts/vf/public/stix/ot1-stixgeneralsc.vf
%{_texmfdistdir}/fonts/vf/public/stix/ot2-stixgeneralsc-bold.vf
%{_texmfdistdir}/fonts/vf/public/stix/ot2-stixgeneralsc.vf
%{_texmfdistdir}/fonts/vf/public/stix/t1-stixgeneralsc-bold.vf
%{_texmfdistdir}/fonts/vf/public/stix/t1-stixgeneralsc.vf
%{_texmfdistdir}/tex/latex/stix/ls1stix.fd
%{_texmfdistdir}/tex/latex/stix/ls1stixbb.fd
%{_texmfdistdir}/tex/latex/stix/ls1stixfrak.fd
%{_texmfdistdir}/tex/latex/stix/ls1stixscr.fd
%{_texmfdistdir}/tex/latex/stix/ls1stixsf.fd
%{_texmfdistdir}/tex/latex/stix/ls2stix.fd
%{_texmfdistdir}/tex/latex/stix/ls2stixcal.fd
%{_texmfdistdir}/tex/latex/stix/ls2stixex.fd
%{_texmfdistdir}/tex/latex/stix/ls2stixtt.fd
%{_texmfdistdir}/tex/latex/stix/ot1stix.fd
%{_texmfdistdir}/tex/latex/stix/ot2stix.fd
%{_texmfdistdir}/tex/latex/stix/stix.sty
%{_texmfdistdir}/tex/latex/stix/t1stix.fd
%{_texmfdistdir}/tex/latex/stix/ts1stix.fd
%doc %{_texmfdistdir}/doc/fonts/stix/README
%doc %{_texmfdistdir}/doc/fonts/stix/README.TEXLIVE
%doc %{_texmfdistdir}/doc/fonts/stix/STIX_Font_License_2010.pdf
%doc %{_texmfdistdir}/doc/fonts/stix/stix.pdf
#- source
%doc %{_texmfdistdir}/source/latex/stix/stix.dtx
%doc %{_texmfdistdir}/source/latex/stix/stix.fdd

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
