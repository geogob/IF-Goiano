//	arquivo	teclado.js	-	versão	final
//	Códigos	de	teclas	-	aqui	vão	todos	os	que	forem	necessários
var	SETA_ESQUERDA	=	37;
var	SETA_DIREITA	=	39;
var	ESPACO	=	32;
var ENTER = 13;
var SETA_UP = 40;
var SETA_DOWN = 38;

function	Teclado(elemento)	{
			this.elemento	=	elemento;
			//	Array	de	teclas	pressionadas
			this.pressionadas	=	[];
			//	Array	de	teclas	disparadas
			this.disparadas	=	[];
			//	Funções	de	disparo
			this.funcoesDisparo	=	[];
			var	teclado	=	this;
			elemento.addEventListener('keydown',	function(evento)	{
						var	tecla	=	evento.keyCode;		//	Tornando	mais	legível	;)
						teclado.pressionadas[tecla]	=	true;
						//	Disparar	somente	se	for	o	primeiro	keydown	da	tecla
						if	(teclado.funcoesDisparo[tecla]	&&
										!	teclado.disparadas[tecla])	{
										teclado.disparadas[tecla]	=	true;
										teclado.funcoesDisparo[tecla]	()	;
																}
			});
			
			elemento.addEventListener('keyup',	function(evento)	{
						teclado.pressionadas[evento.keyCode]	=	false;
						teclado.disparadas[evento.keyCode]	=	false;
			});
}
Teclado.prototype	=	{
			pressionada:	function(tecla)	{
						return	this.pressionadas[tecla];
			},
			disparou:	function(tecla,	callback)	{
						this.funcoesDisparo[tecla]	=	callback;
			}
}