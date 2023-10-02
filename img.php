<?php
$arr=file('img.txt');
$n=count($arr);
for ($i=0;$i<$n;$i++) {
    $x = rand(0,$n-1);
    header("Location: ".$arr[$x],"\n");
}
?>
