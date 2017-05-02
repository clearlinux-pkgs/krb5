#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : krb5
Version  : 1.14.4
Release  : 17
URL      : https://github.com/krb5/krb5/archive/krb5-1.14.4-final.tar.gz
Source0  : https://github.com/krb5/krb5/archive/krb5-1.14.4-final.tar.gz
Summary  : An implementation of Kerberos network authentication
Group    : Development/Tools
License  : BSD-2-Clause MIT
Requires: krb5-bin
Requires: krb5-lib
Requires: krb5-data
Requires: krb5-locales
Requires: krb5-doc
BuildRequires : bison
BuildRequires : dejagnu
BuildRequires : e2fsprogs-data
BuildRequires : e2fsprogs-dev
BuildRequires : e2fsprogs-dev32
BuildRequires : e2fsprogs-extras
BuildRequires : expect
BuildRequires : flex
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : groff
BuildRequires : openssl-dev
BuildRequires : openssl-dev32
BuildRequires : python-dev
BuildRequires : readline-dev
BuildRequires : readline-dev32
BuildRequires : yasm

%description
Kerberos Version 5, Release 1.14
Release Notes
The MIT Kerberos Team
---------------------------

%package bin
Summary: bin components for the krb5 package.
Group: Binaries
Requires: krb5-data

%description bin
bin components for the krb5 package.


%package data
Summary: data components for the krb5 package.
Group: Data

%description data
data components for the krb5 package.


%package dev
Summary: dev components for the krb5 package.
Group: Development
Requires: krb5-lib
Requires: krb5-bin
Requires: krb5-data
Provides: krb5-devel

%description dev
dev components for the krb5 package.


%package dev32
Summary: dev32 components for the krb5 package.
Group: Default
Requires: krb5-lib32
Requires: krb5-bin
Requires: krb5-data
Requires: krb5-dev

%description dev32
dev32 components for the krb5 package.


%package doc
Summary: doc components for the krb5 package.
Group: Documentation

%description doc
doc components for the krb5 package.


%package lib
Summary: lib components for the krb5 package.
Group: Libraries
Requires: krb5-data

%description lib
lib components for the krb5 package.


%package lib32
Summary: lib32 components for the krb5 package.
Group: Default
Requires: krb5-data

%description lib32
lib32 components for the krb5 package.


%package locales
Summary: locales components for the krb5 package.
Group: Default

%description locales
locales components for the krb5 package.


%prep
%setup -q -n krb5-krb5-1.14.4-final
pushd ..
cp -a krb5-krb5-1.14.4-final build32
popd

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487965121
pushd src
%reconfigure --disable-static --with-system-es --with-system-et
make V=1  %{?_smp_mflags}
popd
pushd ../build32/src
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%reconfigure --disable-static --with-system-es --with-system-et  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1487965121
rm -rf %{buildroot}
pushd ../build32/src
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd src
%make_install
popd
%find_lang mit-krb5
## make_install_append content
chmod a+x %{buildroot}/usr/bin/ksu
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gss-client
/usr/bin/gss-server
/usr/bin/k5srvutil
/usr/bin/kadmin
/usr/bin/kadmin.local
/usr/bin/kadmind
/usr/bin/kdb5_util
/usr/bin/kdestroy
/usr/bin/kinit
/usr/bin/klist
/usr/bin/kpasswd
/usr/bin/kprop
/usr/bin/kpropd
/usr/bin/kproplog
/usr/bin/krb5-config
/usr/bin/krb5-send-pr
/usr/bin/krb5kdc
/usr/bin/ksu
/usr/bin/kswitch
/usr/bin/ktutil
/usr/bin/kvno
/usr/bin/sclient
/usr/bin/sim_client
/usr/bin/sim_server
/usr/bin/sserver
/usr/bin/uuclient
/usr/bin/uuserver

%files data
%defattr(-,root,root,-)
/usr/share/examples/krb5/kdc.conf
/usr/share/examples/krb5/krb5.conf
/usr/share/examples/krb5/services.append

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/gssapi/gssapi.h
/usr/include/gssapi/gssapi_ext.h
/usr/include/gssapi/gssapi_generic.h
/usr/include/gssapi/gssapi_krb5.h
/usr/include/gssapi/mechglue.h
/usr/include/gssrpc/auth.h
/usr/include/gssrpc/auth_gss.h
/usr/include/gssrpc/auth_gssapi.h
/usr/include/gssrpc/auth_unix.h
/usr/include/gssrpc/clnt.h
/usr/include/gssrpc/netdb.h
/usr/include/gssrpc/pmap_clnt.h
/usr/include/gssrpc/pmap_prot.h
/usr/include/gssrpc/pmap_rmt.h
/usr/include/gssrpc/rename.h
/usr/include/gssrpc/rpc.h
/usr/include/gssrpc/rpc_msg.h
/usr/include/gssrpc/svc.h
/usr/include/gssrpc/svc_auth.h
/usr/include/gssrpc/types.h
/usr/include/gssrpc/xdr.h
/usr/include/kadm5/admin.h
/usr/include/kadm5/chpass_util_strings.h
/usr/include/kadm5/kadm_err.h
/usr/include/krb5/ccselect_plugin.h
/usr/include/krb5/clpreauth_plugin.h
/usr/include/krb5/hostrealm_plugin.h
/usr/include/krb5/kadm5_hook_plugin.h
/usr/include/krb5/kdcpreauth_plugin.h
/usr/include/krb5/krb5.h
/usr/include/krb5/localauth_plugin.h
/usr/include/krb5/locate_plugin.h
/usr/include/krb5/plugin.h
/usr/include/krb5/preauth_plugin.h
/usr/include/krb5/pwqual_plugin.h
/usr/lib64/libgssapi_krb5.so
/usr/lib64/libgssrpc.so
/usr/lib64/libk5crypto.so
/usr/lib64/libkadm5clnt.so
/usr/lib64/libkadm5clnt_mit.so
/usr/lib64/libkadm5srv.so
/usr/lib64/libkadm5srv_mit.so
/usr/lib64/libkdb5.so
/usr/lib64/libkrad.so
/usr/lib64/libkrb5.so
/usr/lib64/libkrb5support.so
/usr/lib64/libverto.so
/usr/lib64/pkgconfig/gssrpc.pc
/usr/lib64/pkgconfig/kadm-client.pc
/usr/lib64/pkgconfig/kadm-server.pc
/usr/lib64/pkgconfig/kdb.pc
/usr/lib64/pkgconfig/krb5-gssapi.pc
/usr/lib64/pkgconfig/krb5.pc
/usr/lib64/pkgconfig/mit-krb5-gssapi.pc
/usr/lib64/pkgconfig/mit-krb5.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libgssapi_krb5.so
/usr/lib32/libgssrpc.so
/usr/lib32/libk5crypto.so
/usr/lib32/libkadm5clnt.so
/usr/lib32/libkadm5clnt_mit.so
/usr/lib32/libkadm5srv.so
/usr/lib32/libkadm5srv_mit.so
/usr/lib32/libkdb5.so
/usr/lib32/libkrad.so
/usr/lib32/libkrb5.so
/usr/lib32/libkrb5support.so
/usr/lib32/libverto.so
/usr/lib32/pkgconfig/32gssrpc.pc
/usr/lib32/pkgconfig/32kadm-client.pc
/usr/lib32/pkgconfig/32kadm-server.pc
/usr/lib32/pkgconfig/32kdb.pc
/usr/lib32/pkgconfig/32krb5-gssapi.pc
/usr/lib32/pkgconfig/32krb5.pc
/usr/lib32/pkgconfig/32mit-krb5-gssapi.pc
/usr/lib32/pkgconfig/32mit-krb5.pc
/usr/lib32/pkgconfig/gssrpc.pc
/usr/lib32/pkgconfig/kadm-client.pc
/usr/lib32/pkgconfig/kadm-server.pc
/usr/lib32/pkgconfig/kdb.pc
/usr/lib32/pkgconfig/krb5-gssapi.pc
/usr/lib32/pkgconfig/krb5.pc
/usr/lib32/pkgconfig/mit-krb5-gssapi.pc
/usr/lib32/pkgconfig/mit-krb5.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*
%exclude /usr/share/man/man5/.k5identity.5
%exclude /usr/share/man/man5/.k5login.5

%files lib
%defattr(-,root,root,-)
/usr/lib64/krb5/plugins/kdb/db2.so
/usr/lib64/krb5/plugins/preauth/otp.so
/usr/lib64/krb5/plugins/preauth/pkinit.so
/usr/lib64/krb5/plugins/preauth/test.so
/usr/lib64/krb5/plugins/tls/k5tls.so
/usr/lib64/libgssapi_krb5.so.2
/usr/lib64/libgssapi_krb5.so.2.2
/usr/lib64/libgssrpc.so.4
/usr/lib64/libgssrpc.so.4.2
/usr/lib64/libk5crypto.so.3
/usr/lib64/libk5crypto.so.3.1
/usr/lib64/libkadm5clnt_mit.so.10
/usr/lib64/libkadm5clnt_mit.so.10.0
/usr/lib64/libkadm5srv_mit.so.10
/usr/lib64/libkadm5srv_mit.so.10.0
/usr/lib64/libkdb5.so.8
/usr/lib64/libkdb5.so.8.0
/usr/lib64/libkrad.so.0
/usr/lib64/libkrad.so.0.0
/usr/lib64/libkrb5.so.3
/usr/lib64/libkrb5.so.3.3
/usr/lib64/libkrb5support.so.0
/usr/lib64/libkrb5support.so.0.1
/usr/lib64/libverto.so.0
/usr/lib64/libverto.so.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/krb5/plugins/kdb/db2.so
/usr/lib32/krb5/plugins/preauth/otp.so
/usr/lib32/krb5/plugins/preauth/pkinit.so
/usr/lib32/krb5/plugins/preauth/test.so
/usr/lib32/krb5/plugins/tls/k5tls.so
/usr/lib32/libgssapi_krb5.so.2
/usr/lib32/libgssapi_krb5.so.2.2
/usr/lib32/libgssrpc.so.4
/usr/lib32/libgssrpc.so.4.2
/usr/lib32/libk5crypto.so.3
/usr/lib32/libk5crypto.so.3.1
/usr/lib32/libkadm5clnt_mit.so.10
/usr/lib32/libkadm5clnt_mit.so.10.0
/usr/lib32/libkadm5srv_mit.so.10
/usr/lib32/libkadm5srv_mit.so.10.0
/usr/lib32/libkdb5.so.8
/usr/lib32/libkdb5.so.8.0
/usr/lib32/libkrad.so.0
/usr/lib32/libkrad.so.0.0
/usr/lib32/libkrb5.so.3
/usr/lib32/libkrb5.so.3.3
/usr/lib32/libkrb5support.so.0
/usr/lib32/libkrb5support.so.0.1
/usr/lib32/libverto.so.0
/usr/lib32/libverto.so.0.0

%files locales -f mit-krb5.lang
%defattr(-,root,root,-)

