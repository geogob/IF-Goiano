//	arquivo:	carro.js
//	Função	construtora
function Bolada( cor, velocMedia){
			this.cor	=	cor;
			this.raio = 10;
			this.velocMedia	=	velocMedia;
			this.x = 10;
			this.y = 10;
}

//	Prototype	com	os	métodos
Bolada.prototype	= {
			mover: function() {
				this.x += 5;
				this.y += 5;
			},

			explodir: function() {
				this.x = 0;
				this.y = 0;
			}
}