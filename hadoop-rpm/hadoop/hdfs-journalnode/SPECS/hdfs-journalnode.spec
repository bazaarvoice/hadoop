# rpmrebuild autogenerated specfile

%define defaultbuildroot /
AutoProv: no
%undefine __find_provides
AutoReq: no
%undefine __find_requires
# Do not try autogenerate prereq/conflicts/obsoletes and check files
%undefine __check_files
%undefine __find_prereq
%undefine __find_conflicts
%undefine __find_obsoletes
# Be sure buildpolicy set to do nothing
%define __spec_install_post %{nil}
# Something that need for rpm-4.1
%define _missing_doc_files_terminate_build 0
#dummy
#dummy
#BUILDHOST:    c66-slave-ff632c10-2.novalocal
#BUILDTIME:    Wed May 31 03:44:45 2017
#SOURCERPM:    hadoop_2_6_1_0_129-2.7.3.2.6.1.0-129.src.rpm

#RPMVERSION:   4.8.0



#OS:           linux
#SIZE:           6659
#ARCHIVESIZE:           7340
#ARCH:         x86_64
BuildArch:     x86_64
Name:          hadoop_2_6_1_0_129-hdfs-journalnode
Version:       2.7.3.2.6.1.0
Release:       129
License:       Apache License v2.0 
Group:         System/Daemons
Summary:       Hadoop HDFS JournalNode


URL:           http://hadoop.apache.org/core/







Provides:      hadoop_2_6_1_0_129-hdfs-journalnode = 2.7.3.2.6.1.0-129
Provides:      hadoop_2_6_1_0_129-hdfs-journalnode(x86-64) = 2.7.3.2.6.1.0-129
Requires:      hadoop_2_6_1_0_129-hdfs = 2.7.3.2.6.1.0-129
Requires:      hadoop_2_6_1_0_129 = 2.7.3.2.6.1.0-129
#Requires:      rpmlib(FileDigests) <= 4.6.0-1
#Requires:      rpmlib(PayloadFilesHavePrefix) <= 4.0-1
#Requires:      rpmlib(CompressedFileNames) <= 3.0.4-1
Requires:      /bin/bash  
#Requires:      rpmlib(PayloadIsXz) <= 5.2-1
#suggest
#enhance
%description
The HDFS JournalNode is responsible for persisting NameNode edit logs.
In a typical deployment the JournalNode daemon runs on at least three
separate machines in the cluster.
%files
%config(noreplace) %attr(0644, root, root) "/usr/hdp/2.6.1.0-129/etc/default/hadoop-hdfs-journalnode"
%attr(0755, root, root) "/usr/hdp/2.6.1.0-129/hadoop-hdfs/etc/rc.d/init.d/hadoop-hdfs-journalnode"
%attr(0600, root, root) "/usr/hdp/2.6.1.0-129/hadoop-hdfs/usr/lib/systemd/system/hadoop-hdfs-journalnode.service"
%changelog
