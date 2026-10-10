<?php
function searchWebData($url, $data_type, $file_type) {
    $response = file_get_contents("$url?data_type=$data_type&file_type=$file_type");
    return $response;
}

echo "Digite a URL: ";
$url = trim(fgets(STDIN));
echo "Digite o tipo de dado: ";
$data_type = trim(fgets(STDIN));
echo "Digite o tipo de arquivo: ";
$file_type = trim(fgets(STDIN));

$result = searchWebData($url, $data_type, $file_type);
echo $result;
?>
