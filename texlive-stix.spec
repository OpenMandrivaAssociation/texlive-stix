%global tl_name stix
%global tl_revision 79618
%global tl_version 1.1.3

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	OpenType Unicode maths fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/stix
License:	ofl lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stix.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stix.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stix.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The STIX fonts are a suite of unicode OpenType fonts containing a
complete set of mathematical glyphs. As of April 2018 this package is
considered obsolete. See stix2-otf and stix2-type1 instead.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from stix:
Map stix.map
TL_DROPIN_EOF
