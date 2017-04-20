%undefine _missing_build_ids_terminate_build
%define debug_package   %{nil}

Name:           hiback
Version:        S961su2613
Release:        1%{?dist}
Summary:        Hiback backup client for Linux x64 servers RHEL6

Group:          Applications/System
License:        Hiback proprietary
URL:            http://stoge.pn.tieto.com/versiot/unixver.html
Source0:        http://192.168.2.9:8081/artifactory/S961su2613.x64-1.0.1.tar
Source1:        http://192.168.2.9:8081/artifactory/hiserv
Source2:        http://192.168.2.9:8081/artifactory/cleanxfiles.tar

BuildRoot:      $RPM_BUILD_ROOT
BuildArch:      x86_64
AutoReq:        0
BuildRequires:  /bin/rm, /bin/mkdir, /bin/cp, /bin/sed
Requires:       /bin/bash, /bin/sh
%{?el6:Requires:        /usr/sbin/xinetd}
%{?el6:Requires:        /usr/sbin/crond}

%description
Hiback backup client for Linux x64 servers RHEL6

%prep
%setup -q -c -n %{name}-%{version}
%setup -q -D -T -a 2

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc
mkdir -p $RPM_BUILD_ROOT/etc/xinetd.d
mkdir -p $RPM_BUILD_ROOT/opt
mkdir -p $RPM_BUILD_ROOT/opt/Hiback
mkdir -p $RPM_BUILD_ROOT/opt/Hiback/{acsls,adabas,db2,mm,msg,onbar,oracle,oracle                                                                                                                                                             8,orahot,tape,tapeserver,tmp,tools,list,log,backint,conf}
install Hiback/{message.cat,message.catd,message.cate,message.cati,xhibackd,tape                                                                                                                                                             mac,tapemax,svchghost,svfold,svinjuke,clearlog,automax,automac,consort,medmax,mp                                                                                                                                                             xinfo,app_inetd.tpl,app_services.tpl,CONDEV.def,CONDEV.tpl,dontstore.tpl,exitcod                                                                                                                                                             es,finHib,grpnam,Hbfr,help.txt,help.txtd,help.txte,help.txti,Hiback,Hibackp,Hibs                                                                                                                                                             hr,hiserv,perfh,recall,reply,replypid,secure.cfg,secure.cfg.tpl,svc,README} $RPM                                                                                                                                                             _BUILD_ROOT/opt/Hiback
install Hiback/CONDEV.tpl $RPM_BUILD_ROOT/opt/Hiback/CONDEV
install %{SOURCE1} $RPM_BUILD_ROOT/etc/xinetd.d
install Hiback/acsls/{mini_el,ssi,start_ssi.sh,t_parent,t_ssi.sh} $RPM_BUILD_ROO                                                                                                                                                             T/opt/Hiback/acsls
install Hiback/adabas/{ada_bak,hibad.mydb.in,pre_dump_full_application,rest.sh}                                                                                                                                                              $RPM_BUILD_ROOT/opt/Hiback/adabas
install Hiback/db2/{db2.tpl,dv,dv.x,libdb2api.sl,vdb,v.x} $RPM_BUILD_ROOT/opt/Hi                                                                                                                                                             back/db2
install Hiback/mm/{mmf,muf,putMM}  $RPM_BUILD_ROOT/opt/Hiback/mm
install Hiback/onbar/{dv,dv.x,libBSA.sl,onbar.tpl,von,v.x,zx,zy} $RPM_BUILD_ROOT                                                                                                                                                             /opt/Hiback/onbar
install Hiback/oracle/{dv,dv.x,libora.sl,oracle.tpl,reqs,vor,v.x} $RPM_BUILD_ROO                                                                                                                                                             T/opt/Hiback/oracle
install Hiback/oracle8/{dv,dv.x,libora.sl,oracle.tpl,reqs,vor,v.x} $RPM_BUILD_RO                                                                                                                                                             OT/opt/Hiback/oracle8
install Hiback/orahot/{orahot,orahot.ini.tpl,orapost.sh.tpl,orapre.sh.tpl,README                                                                                                                                                             } $RPM_BUILD_ROOT/opt/Hiback/orahot
install Hiback/tape/{checkmega,default_stack.tpl,prot,stl_bul,tpm,checktape,hija                                                                                                                                                             cc,stack_examples,stl_ser,das.cfg.tpl,opMTX,stk.tpl,tape.defs.tpl} $RPM_BUILD_RO                                                                                                                                                             OT/opt/Hiback/tape
install Hiback/tapeserver/{hidin,hidout,hidst,hidst_gig,hidstper,multiplexer.tpl                                                                                                                                                             ,watchdog} $RPM_BUILD_ROOT/opt/Hiback/tapeserver
install Hiback/tools/{clHib,invkuk,message.e,odskf,svmerge,swit,disptpd,kuk,mess                                                                                                                                                             age.i,odsks,svmerger-ux,undocat,ffix,message.d,mkcat,STATUS,svreset} $RPM_BUILD_                                                                                                                                                             ROOT/opt/Hiback/tools
install Hiback/backint/{backint,label.ind,par_file.tpl,pool.tpl,showlog,splitfil                                                                                                                                                             e.tpl,volmgr} $RPM_BUILD_ROOT/opt/Hiback/backint
install Hiback/conf/{opibmbox,opseqbox,box_examples,default_box.tpl} $RPM_BUILD_                                                                                                                                                             ROOT/opt/Hiback/conf
cp -R %{_builddir}/%{name}-%{version}/mcs $RPM_BUILD_ROOT/opt/Hiback

%clean
rm -rf $RPM_BUILD_ROOT

%files
# We want to use the %ghost directive for log files.
# We want to use the %dir directive for directories.
# We want to use the %config directive for specifying the configuration files.
%defattr(-,root,root,-)
%config(noreplace) /opt/Hiback/conf/*
%config(noreplace) %attr(644, root, root) /etc/xinetd.d/hiserv
/opt/Hiback/app_inetd.tpl
/opt/Hiback/app_services.tpl
/opt/Hiback/automac
/opt/Hiback/automax
/opt/Hiback/clearlog
/opt/Hiback/CONDEV.def
/opt/Hiback/CONDEV.tpl
%attr(444,root,root) /opt/Hiback/CONDEV
/opt/Hiback/consort
%config(missingok) /opt/Hiback/dontstore.tpl
/opt/Hiback/exitcodes
/opt/Hiback/finHib
/opt/Hiback/grpnam
/opt/Hiback/Hbfr
/opt/Hiback/help.txt
/opt/Hiback/help.txtd
/opt/Hiback/help.txte
/opt/Hiback/help.txti
/opt/Hiback/Hiback
/opt/Hiback/Hibackp
/opt/Hiback/Hibshr
/opt/Hiback/hiserv
/opt/Hiback/medmax
/opt/Hiback/message.cat
/opt/Hiback/message.catd
/opt/Hiback/message.cate
/opt/Hiback/message.cati
/opt/Hiback/mpxinfo
/opt/Hiback/perfh
/opt/Hiback/recall
/opt/Hiback/reply
/opt/Hiback/replypid
/opt/Hiback/secure.cfg
/opt/Hiback/secure.cfg.tpl
/opt/Hiback/svc
/opt/Hiback/svchghost
/opt/Hiback/svfold
/opt/Hiback/svinjuke
/opt/Hiback/tapemac
/opt/Hiback/tapemax
/opt/Hiback/xhibackd
/opt/Hiback/mcs/*
/opt/Hiback/backint/*
/opt/Hiback/tools/*
%config(missingok) /opt/Hiback/tapeserver/hidst
%config(missingok) /opt/Hiback/tapeserver/hidin
%config(missingok) /opt/Hiback/tapeserver/hidout
%ghost %attr(664,root,root) /opt/Hiback/log/Hiback.log
%ghost %attr(664,root,root) /opt/Hiback/log/hiserv.log
%ghost %attr(664,root,root) /opt/Hiback/log/hibens.log
/opt/Hiback/tapeserver/*
/opt/Hiback/tape/*
/opt/Hiback/acsls/*
/opt/Hiback/adabas/*
/opt/Hiback/db2/*
/opt/Hiback/mm/*
/opt/Hiback/onbar/*
/opt/Hiback/oracle/*
/opt/Hiback/oracle8/*
/opt/Hiback/orahot/*
%doc /opt/Hiback/README

%pre
crontab -l > mycron
grep 'cleanxfiles.sh' mycron || echo -e "00 08 * * * /Hiback/mcs/cleanup/cleanxf                                                                                                                                                             iles.sh >/dev/null 2>&1" >> mycron
crontab mycron
rm mycron

%post
if [ "$1" == "1" ]; then
        if [ ! -L /Hiback ]; then
                ln -s /opt/Hiback /Hiback
        fi

        grep '^hiserv' /etc/services || echo -e "hiserv\t\t32323/tcp\t\t# Hiback                                                                                                                                                             " >> /etc/services
        chkconfig xinetd on

        if (( $(ps -ef | grep -v grep | grep xinetd | wc -l) > 0 ))
        then
                /etc/init.d/xinetd reload > /dev/null
        else
                /etc/init.d/xinetd restart > /dev/null
        fi
        if (( $(ps -ef | grep -v grep | grep crond | wc -l) > 0 ))
        then
                /etc/init.d/crond reload > /dev/null
        else
                /etc/init.d/crond restart > /dev/null
        fi

        cd /opt/Hiback && /bin/sh finHib
        /sbin/ldconfig
        exit 0
fi

%preun
crontab -l > mycron
sed -i -e '/cleanxfiles.sh/d' mycron
crontab mycron
rm mycron

%postun
if [ "$1" == "0" ]; then
        sed -i -e '/hiserv/d' /etc/services
        if [ -L /Hiback ]; then
                rm /Hiback
        fi
        if [ -L /Hibtest ]; then
                rm /Hibtest
        fi

        if (( $(ps -ef | grep -v grep | grep xinetd | wc -l) > 0 ))
        then
                /etc/init.d/xinetd reload > /dev/null
        else
                /etc/init.d/xinetd restart > /dev/null
        fi

        if (( $(ps -ef | grep -v grep | grep crond | wc -l) > 0 ))
        then
                /etc/init.d/crond reload > /dev/null
        else
                /etc/init.d/crond restart > /dev/null
        fi

        rm -f /etc/xinetd.d/hiserv
        rm -rf /opt/Hiback
        rm -rf /opt/Hibtest
        /sbin/ldconfig
        exit 0
fi

%changelog
* Thu Apr 20 2016 Karthick Murugadhas <karthickmurugadhas@gmail.com> - 1.0-1
- Initial Build