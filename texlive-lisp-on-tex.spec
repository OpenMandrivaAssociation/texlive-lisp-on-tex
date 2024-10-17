Name:		texlive-lisp-on-tex
Version:	38722
Release:	2
Summary:	Execute LISP code in a LaTeX document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lisp-on-tex
License:	BSD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lisp-on-tex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lisp-on-tex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a LISP interpreter written using TeX
macros; it is provided as a LaTeX package. The interpreter
static scoping, dynamic typing, and eager evaluation.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/lisp-on-tex
%doc %{_texmfdistdir}/doc/latex/lisp-on-tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
