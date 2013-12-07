# revision 30447
# category Package
# catalog-ctan /macros/latex/contrib/preprint
# catalog-date 2013-05-13 11:38:32 +0200
# catalog-license collection
# catalog-version 2011
Name:		texlive-preprint
Epoch:		1
Version:	2011
Release:	4
Summary:	A bundle of packages provided "as is"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/preprint
License:	COLLECTION
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/preprint.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/preprint.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/preprint.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle comprises: - authblk, which permits footnote style
author/affiliation input in the \author command, - balance, to
balance the end of \twocolumn pages, - figcaps, to send figure
captions, etc., to end document, - fullpage, to set narrow page
margins and set a fixed page style, and - sublabel, which
permits counters to be subnumbered.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/preprint/authblk.sty
%{_texmfdistdir}/tex/latex/preprint/balance.sty
%{_texmfdistdir}/tex/latex/preprint/figcaps.sty
%{_texmfdistdir}/tex/latex/preprint/fullpage.sty
%{_texmfdistdir}/tex/latex/preprint/sublabel.sty
%doc %{_texmfdistdir}/doc/latex/preprint/README
%doc %{_texmfdistdir}/doc/latex/preprint/authblk.pdf
%doc %{_texmfdistdir}/doc/latex/preprint/balance.pdf
%doc %{_texmfdistdir}/doc/latex/preprint/figcaps.pdf
%doc %{_texmfdistdir}/doc/latex/preprint/fullpage.pdf
%doc %{_texmfdistdir}/doc/latex/preprint/sublabel.pdf
#- source
%doc %{_texmfdistdir}/source/latex/preprint/authblk.drv
%doc %{_texmfdistdir}/source/latex/preprint/authblk.dtx
%doc %{_texmfdistdir}/source/latex/preprint/authblk.ins
%doc %{_texmfdistdir}/source/latex/preprint/balance.drv
%doc %{_texmfdistdir}/source/latex/preprint/balance.dtx
%doc %{_texmfdistdir}/source/latex/preprint/balance.ins
%doc %{_texmfdistdir}/source/latex/preprint/figcaps.drv
%doc %{_texmfdistdir}/source/latex/preprint/figcaps.dtx
%doc %{_texmfdistdir}/source/latex/preprint/figcaps.ins
%doc %{_texmfdistdir}/source/latex/preprint/fullpage.drv
%doc %{_texmfdistdir}/source/latex/preprint/fullpage.dtx
%doc %{_texmfdistdir}/source/latex/preprint/fullpage.ins
%doc %{_texmfdistdir}/source/latex/preprint/sublabel.drv
%doc %{_texmfdistdir}/source/latex/preprint/sublabel.dtx
%doc %{_texmfdistdir}/source/latex/preprint/sublabel.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
