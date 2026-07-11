%global tl_name stix
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.3
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
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The STIX fonts are a suite of unicode OpenType fonts containing a
complete set of mathematical glyphs. As of April 2018 this package is
considered obsolete. See stix2-otf and stix2-type1 instead.

