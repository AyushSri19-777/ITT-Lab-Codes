#perl 5.22.1 
@arr=(1,2,3,4,5);
print $arr[-1];
print "\n",$arr[$#arr];
print "\n",@arr;
push(@arr,(6,7,8,9));
print"\n", @arr;
pop(@arr);
print"\n", @arr;
scalar(@arr);
print"\n",scalar(@arr);
unshift(@arr,6);
print "\n",@arr;
shift(@arr);
print "\n",@arr;
@b=(1,2,3);
print "\n",@b;
$c=shift(@b);
push(@b,$c);
print "\n",@b,"\n";
%hash=("Ayush"=>"Kavya","Rishabh"=>"Ishika","Varun"=>"Shubham");
print $hash{"Ayush"};
@keyhash=keys%hash;
@valhash=values%hash;
print "\n",@keyhash,"\n";
print @valhash;
@ab=(1,2,3,4,5,6);
print "\n",@ab;
$#ab-=2;
print "\n",@ab;
$name="ayush";
$name1="AYUSH";
$name1=lc($name1);
print "\n",$name1,"\n";
$name="Kavya";
print "$name loves saying Ayush Ayush Ayush!!\n";
$a=25;
print "$a din mein paisa double\n";
$a=22;
print $a-4,"\n";
$b="50";
print $b+10,"\n";
print '2'+'3',"\n";
$a="Ayush Srivastava\n";
$b=substr($a,3);
print $b,"\n";
print chr(65);
$f=chomp($a);
print $f,"\n";
print rindex($a,"va",15),"\n";
@a=(1,2,3,4,5);
print join("<",@a);
$a="ayushugytu";
@g=split("u",$a);
print "\n",join(" ",@g),"\n";
$i=5;
#print $i;
while($i gt -1)
{
    print $i,"\n";
    $i--;
}
print "Hello\n";
for $i(0..5)
{
    print "$i\n";
}
@arr=("Bob","Vagene","Amrit");
sub numeric{
    return $a cmp $b;
}
print join(" ",sort numeric @arr);
foreach $ele(@arr)
{
    print $ele,"\n";
}
$a="ayushugytu";
@arr=split(/u/,$a);
print join(" ",@arr),"\n";
@arr=([1,2,3],[4,5,6],[7,8,9]);
for $i(0..2){
for $j(0..2){
if($i eq $j){
print $arr[$i][$j],"\n";
}
}
}
sub add
{
return $a+$b;
}
$a=<STDIN>;
$b=<STDIN>;
print "The sum is : ",add;
sub Avg{
$n=scalar(@_);
foreach $i(@_)
{
$sum+=$i;
}
return $sum/$n;
}
print "\nThe Average:",Avg(1,3,5,7),"\n";
@arr=();
sub joinmaadi{
my %hash=@_;
foreach $key(keys%hash){
push(@arr,$hash{$key});
}
print join(" ",(sort @arr));
}
joinmaadi("Ayush"=>"Kavya","Shubham"=>"Varun","Rishabh"=>"Shivano");
$a="ayush you are the soniye of the night and you are ayush the shining star";
@arr=split(" ",$a);
#%ayu=();
#push(%ayu,("Ayus"=>0));
@arr=();
push(@arr,1);
push(@arr,3);
push(@arr,2);
print "\n",@arr;
@arr=();
sub test{
my %hash=@_;
$n=scalar(@_);
print "Size: $n\n";
foreach $key(keys%hash)
{
push(@arr,$key."loves".$hash{$key});
}
print join("-->",sort @arr);
}
test("Ayush"=>"Kavya","Shubham"=>"Varun","Rishabh"=>"Shivano");
sub tet
{
    @lis=@_;
    $sum=0;
    $n=scalar(@_);
    foreach $i(@lis)
    {
        $sum+=$i;
    }
 print "\nSum : $sum\n";
 }
@c=(1,2,3,4,5,6,7);
tet(@c);
$a="\n65ayush baby babyyy baybyy is096 love cuteis ^ AyushB78";
print "$a\n";
$a=~ s/[^y0-5]/are/g;
print "$a\n";
$a=~ tr/abc/xyz/;
print "$a\n";
$a="\n65ayush baby babyyy baybyy bab is096 babyy love cuteis cut AyushB78";
$a=~ s/baby{2}|cut+/asli/g;
print "$a\n";
$b="a-b!c!d-";
$b=~s/a(.)b(.)c\2d\1/Found/;

#5
5
12345
123456789
12345678
8
612345678
12345678
123
231
Kavya
RishabhVarunAyush
IshikaShubhamKavya
123456
1234
ayush
Kavya loves saying Ayush Ayush Ayush!!
25 din mein paisa double
18
60
5
sh Srivastava

A1
14
1<2<3<4<5
ay sh gyt
5
4
3
2
1
0
Hello
0
1
2
3
4
5
Amrit Bob VageneBob
Vagene
Amrit
ay sh gyt
1
5
9
The sum is : 8
The Average:4
Kavya Shivano Varun
132Size: 6
AyushlovesKavya-->RishabhlovesShivano-->ShubhamlovesVarun
Sum : 28

65ayush baby babyyy baybyy is096 love cuteis ^ AyushB78
areare5areyareareareareareareareyareareareareyyyareareareyareyyareareare0areareareareareareareareareareareareareareareareareareyareareareareareare
xrexre5xreyxrexrexrexrexrexrexreyxrexrexrexreyyyxrexrexreyxreyyxrexrexre0xrexrexrexrexrexrexrexrexrexrexrexrexrexrexrexrexrexreyxrexrexrexrexrexre

#65ayush baby asliy baybyy bab is096 asli love aslieis asli AyushB78

#Length: 3/82