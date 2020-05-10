<?php 

include_once 'lib/nusoap.php'; 
$servicio = new soap_server();

$ns = "urn:webService";
$servicio->configureWSDL("Soap Php Servicio", $ns);

$servicio->schemaTargetNamespace = $ns;

$servicio->register("FuncionSaludo", array('Nombres' => 'xsd:string', 'ApellidoP' => 'xsd:string', 'ApellidoM' => 'xsd:string', 'Sexo' => 'xsd:string'), array('return' => 'xsd:string'));
 
$servicio->register("FuncionRut", array('Rut' => 'xsd:string'), array('return' => 'xsd:string'), $ns);

function FuncionSaludo($Nombres, $ApellidoP, $ApellidoM, $Sexo){

	$Saludo = $Nombres . ' ' . $ApellidoP . ' ' . $ApellidoM;

	if($Sexo === 'M' || $Sexo === 'm'){
		return 'Hola Sr. ' . ucwords(strtolower($Saludo));
	}elseif($Sexo === 'f' || $Sexo === 'F'){
		return 'Hola Sra. ' . ucwords(strtolower($Saludo));
	}else{
		return 'Hola ' . ucwords(strtolower($Saludo));
	}

}

function FuncionRut($Rut){
	
	$stringarreglo = 	str_split($Rut, 1); 
	$digVerificador = end($stringarreglo); 
	$Valoriserie = 2; 
	$Sumamodulo = 0;
	$nPrecedentesRut = 0; 

	for ($i=0; $i < strlen($Rut); $i++) { 
		if($stringarreglo[$i] == '-'){
			$nPrecedentesRut =  $i;
		}
	}

	$TruncarRut = array_slice($stringarreglo, 0, $nPrecedentesRut);
	$DarVueltaArreglo = array_reverse($TruncarRut);

	$contador = 0; 

	while ($contador < $nPrecedentesRut) {	
		if($Valoriserie < 8){
			if($DarVueltaArreglo[$contador]=='.'){
				$contador++;
			}else{
				$multiplicacion = $Valoriserie  * intval($DarVueltaArreglo[$contador]);
				$Sumamodulo = $Sumamodulo + $multiplicacion;
				$contador++;
				$Valoriserie++;
				$multiplicacion = 0;
			}

				
		}else{
			$Valoriserie= 2;
		}
	}
	$Elmodulo = $Sumamodulo % 11;;
	$FinalDigito = 11 - $Elmodulo;

	$Validado = 'X';

	if($FinalDigito == 11){
		$Validado = '0';
	}elseif ($FinalDigito == 10){
		$Validado = 'K';
	}else{
		$Validado = strval($FinalDigito);
	}

	$Respuesta = '0';

	if(strcasecmp($Validado, $digVerificador) == 0){
		$Respuesta = 'El Rut consultado es valido';
	}else{
		$Respuesta = 'El Rut consultado es invalido, verifique el Rut';
	}

	return $Respuesta;
}

$httpPost = file_get_contents( 'php://input' ); 
$servicio->service($httpPost);



 ?>