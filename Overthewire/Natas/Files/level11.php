#!/usr/bin/php
<?php

$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");


function xor_encrypt($in,$key) {
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$ciphertext = hex2bin('0a554b221e00482b02044f2503131a70531957685d555a2d121854250355026852115e2c17115e680c');
$plaintext = json_encode($defaultdata);

#echo(xor_encrypt($ciphertext,$plaintext));
$key = 'qw8J';
$good_plaintext = json_encode(array("showpassword"=>"yes","bgcolor"=>"#ffffff"));
echo(base64_encode(xor_encrypt($good_plaintext,$key)));

?>
