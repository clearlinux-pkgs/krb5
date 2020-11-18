#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : krb5
Version  : 1.18.3
Release  : 38
URL      : https://github.com/krb5/krb5/archive/krb5-1.18.3-final/krb5-1.18.3.tar.gz
Source0  : https://github.com/krb5/krb5/archive/krb5-1.18.3-final/krb5-1.18.3.tar.gz
Summary  : An implementation of Kerberos network authentication
Group    : Development/Tools
License  : BSD-2-Clause MIT
Requires: krb5-bin = %{version}-%{release}
Requires: krb5-data = %{version}-%{release}
Requires: krb5-lib = %{version}-%{release}
Requires: krb5-license = %{version}-%{release}
Requires: krb5-locales = %{version}-%{release}
Requires: krb5-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : cyrus-sasl-dev
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
BuildRequires : keyutils-dev
BuildRequires : lmdb-dev
BuildRequires : openldap-dev
BuildRequires : openssl-dev
BuildRequires : openssl-dev32
BuildRequires : pkg-config
BuildRequires : readline-dev
BuildRequires : readline-dev32
BuildRequires : tcl-dev
BuildRequires : yasm

%description
Kerberos Version 5, Release 1.18
Release Notes
The MIT Kerberos Team
---------------------------

%package bin
Summary: bin components for the krb5 package.
Group: Binaries
Requires: krb5-data = %{version}-%{release}
Requires: krb5-license = %{version}-%{release}

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
Requires: krb5-lib = %{version}-%{release}
Requires: krb5-bin = %{version}-%{release}
Requires: krb5-data = %{version}-%{release}
Provides: krb5-devel = %{version}-%{release}
Requires: krb5 = %{version}-%{release}

%description dev
dev components for the krb5 package.


%package dev32
Summary: dev32 components for the krb5 package.
Group: Default
Requires: krb5-lib32 = %{version}-%{release}
Requires: krb5-bin = %{version}-%{release}
Requires: krb5-data = %{version}-%{release}
Requires: krb5-dev = %{version}-%{release}

%description dev32
dev32 components for the krb5 package.


%package lib
Summary: lib components for the krb5 package.
Group: Libraries
Requires: krb5-data = %{version}-%{release}
Requires: krb5-license = %{version}-%{release}

%description lib
lib components for the krb5 package.


%package lib32
Summary: lib32 components for the krb5 package.
Group: Default
Requires: krb5-data = %{version}-%{release}
Requires: krb5-license = %{version}-%{release}

%description lib32
lib32 components for the krb5 package.


%package license
Summary: license components for the krb5 package.
Group: Default

%description license
license components for the krb5 package.


%package locales
Summary: locales components for the krb5 package.
Group: Default

%description locales
locales components for the krb5 package.


%package man
Summary: man components for the krb5 package.
Group: Default

%description man
man components for the krb5 package.


%prep
%setup -q -n krb5-krb5-1.18.3-final
cd %{_builddir}/krb5-krb5-1.18.3-final
pushd ..
cp -a krb5-krb5-1.18.3-final build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605728248
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
pushd src
%reconfigure --disable-static --with-system-es --with-system-et --with-ldap
make  %{?_smp_mflags}
popd
pushd ../build32/src
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%reconfigure --disable-static --with-system-es --with-system-et --with-ldap --with-system-es --with-system-et --without-ldap --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1605728248
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/krb5
cp %{_builddir}/krb5-krb5-1.18.3-final/NOTICE %{buildroot}/usr/share/package-licenses/krb5/d7ec65af3afb6367446a1bb55431b22ab8af401e
cp %{_builddir}/krb5-krb5-1.18.3-final/src/lib/gssapi/LICENSE %{buildroot}/usr/share/package-licenses/krb5/feb23c7f425c7c619cb04c91997f471e2d3b8e9b
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
## Remove excluded files
rm -f %{buildroot}/usr/bin/compile_et
rm -f %{buildroot}/usr/include/com_err.h
rm -f %{buildroot}/usr/lib64/libcom_err.so
rm -f %{buildroot}/usr/share/et/et_c.awk
rm -f %{buildroot}/usr/share/et/et_h.awk
rm -f %{buildroot}/usr/share/man/man5/.k5identity.5
rm -f %{buildroot}/usr/share/man/man5/.k5login.5
## install_append content
chmod a+x %{buildroot}/usr/bin/ksu
## install_append end

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
/usr/bin/kdb5_ldap_util
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
/usr/include/gssapi.h
/usr/include/gssapi/gssapi.h
/usr/include/gssapi/gssapi_alloc.h
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
/usr/include/kdb.h
/usr/include/krad.h
/usr/include/krb5.h
/usr/include/krb5/ccselect_plugin.h
/usr/include/krb5/certauth_plugin.h
/usr/include/krb5/clpreauth_plugin.h
/usr/include/krb5/hostrealm_plugin.h
/usr/include/krb5/kadm5_auth_plugin.h
/usr/include/krb5/kadm5_hook_plugin.h
/usr/include/krb5/kdcpolicy_plugin.h
/usr/include/krb5/kdcpreauth_plugin.h
/usr/include/krb5/krb5.h
/usr/include/krb5/localauth_plugin.h
/usr/include/krb5/locate_plugin.h
/usr/include/krb5/plugin.h
/usr/include/krb5/preauth_plugin.h
/usr/include/krb5/pwqual_plugin.h
/usr/include/profile.h
/usr/include/verto-module.h
/usr/include/verto.h
/usr/lib64/libgssapi_krb5.so
/usr/lib64/libgssrpc.so
/usr/lib64/libk5crypto.so
/usr/lib64/libkadm5clnt.so
/usr/lib64/libkadm5clnt_mit.so
/usr/lib64/libkadm5srv.so
/usr/lib64/libkadm5srv_mit.so
/usr/lib64/libkdb5.so
/usr/lib64/libkdb_ldap.so
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

%files lib
%defattr(-,root,root,-)
/usr/lib64/krb5/plugins/kdb/db2.so
/usr/lib64/krb5/plugins/kdb/kldap.so
/usr/lib64/krb5/plugins/kdb/klmdb.so
/usr/lib64/krb5/plugins/preauth/otp.so
/usr/lib64/krb5/plugins/preauth/pkinit.so
/usr/lib64/krb5/plugins/preauth/spake.so
/usr/lib64/krb5/plugins/preauth/test.so
/usr/lib64/krb5/plugins/tls/k5tls.so
/usr/lib64/libgssapi_krb5.so.2
/usr/lib64/libgssapi_krb5.so.2.2
/usr/lib64/libgssrpc.so.4
/usr/lib64/libgssrpc.so.4.2
/usr/lib64/libk5crypto.so.3
/usr/lib64/libk5crypto.so.3.1
/usr/lib64/libkadm5clnt_mit.so.12
/usr/lib64/libkadm5clnt_mit.so.12.0
/usr/lib64/libkadm5srv_mit.so.12
/usr/lib64/libkadm5srv_mit.so.12.0
/usr/lib64/libkdb5.so.10
/usr/lib64/libkdb5.so.10.0
/usr/lib64/libkdb_ldap.so.1
/usr/lib64/libkdb_ldap.so.1.0
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
/usr/lib32/krb5/plugins/preauth/spake.so
/usr/lib32/krb5/plugins/preauth/test.so
/usr/lib32/krb5/plugins/tls/k5tls.so
/usr/lib32/libgssapi_krb5.so.2
/usr/lib32/libgssapi_krb5.so.2.2
/usr/lib32/libgssrpc.so.4
/usr/lib32/libgssrpc.so.4.2
/usr/lib32/libk5crypto.so.3
/usr/lib32/libk5crypto.so.3.1
/usr/lib32/libkadm5clnt_mit.so.12
/usr/lib32/libkadm5clnt_mit.so.12.0
/usr/lib32/libkadm5srv_mit.so.12
/usr/lib32/libkadm5srv_mit.so.12.0
/usr/lib32/libkdb5.so.10
/usr/lib32/libkdb5.so.10.0
/usr/lib32/libkrad.so.0
/usr/lib32/libkrad.so.0.0
/usr/lib32/libkrb5.so.3
/usr/lib32/libkrb5.so.3.3
/usr/lib32/libkrb5support.so.0
/usr/lib32/libkrb5support.so.0.1
/usr/lib32/libverto.so.0
/usr/lib32/libverto.so.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/krb5/d7ec65af3afb6367446a1bb55431b22ab8af401e
/usr/share/package-licenses/krb5/feb23c7f425c7c619cb04c91997f471e2d3b8e9b

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/k5srvutil.1
/usr/share/man/man1/kadmin.1
/usr/share/man/man1/kdestroy.1
/usr/share/man/man1/kinit.1
/usr/share/man/man1/klist.1
/usr/share/man/man1/kpasswd.1
/usr/share/man/man1/krb5-config.1
/usr/share/man/man1/ksu.1
/usr/share/man/man1/kswitch.1
/usr/share/man/man1/ktutil.1
/usr/share/man/man1/kvno.1
/usr/share/man/man1/sclient.1
/usr/share/man/man5/k5identity.5
/usr/share/man/man5/k5login.5
/usr/share/man/man5/kadm5.acl.5
/usr/share/man/man5/kdc.conf.5
/usr/share/man/man5/krb5.conf.5
/usr/share/man/man7/kerberos.7
/usr/share/man/man8/kadmin.local.8
/usr/share/man/man8/kadmind.8
/usr/share/man/man8/kdb5_ldap_util.8
/usr/share/man/man8/kdb5_util.8
/usr/share/man/man8/kprop.8
/usr/share/man/man8/kpropd.8
/usr/share/man/man8/kproplog.8
/usr/share/man/man8/krb5kdc.8
/usr/share/man/man8/sserver.8

%files locales -f mit-krb5.lang
%defattr(-,root,root,-)

