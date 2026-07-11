%global tl_name preprint
%global tl_revision 30447

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2011
Release:	%{tl_revision}.1
Summary:	A bundle of packages provided as is
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/preprint
License:	collection
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/preprint.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/preprint.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/preprint.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle comprises: authblk, which permits footnote style
author/affiliation input in the \author command, balance, to balance the
end of \twocolumn pages, figcaps, to send figure captions, etc., to end
document, fullpage, to set narrow page margins and set a fixed page
style, and sublabel, which permits counters to be subnumbered.

