import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import * as moment from 'moment';
import { CandleService } from './service/candle/candle.service';
import * as Highcharts from 'highcharts';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'frontend';
  inicialCtrl: FormControl = new FormControl('');
  finalCtrl: FormControl = new FormControl('');
  moedaCtrl: FormControl = new FormControl('');

  moedas = [ 'Real', 'Euro', 'Jpy' ];
  highcharts = Highcharts;
  oneToOne = false;
  update = false;

  respostaValor = [0];
  respostaTempo = [];

  grafico: boolean = false;

  chartOptions: Highcharts.Options = {
    title: {
      text: "Grafico moeda"
    },
    xAxis: {
      categories: this.respostaTempo
    },
    yAxis: {
      title: {
        text: "Valor moeda selecionada perante dolar"
      }
    },
    series: [{
      data: this.respostaValor,
      type: 'line'
    }]
  }

  constructor(
    private candleService: CandleService,
  ) { }

  ngOnInit() {
  }

  click() {

    if (this.finalCtrl.value != '' && this.inicialCtrl.value != '' &&
        this.moedaCtrl.value != '') {
      const date = this.finalCtrl.value.getTime() - this.inicialCtrl.value.getTime()
      if (date > 345600000) {
        alert("Filtro maximo de 5 dias");
      }
      else if (date < 0) {
        alert("Data inicial não pode ser maior que a final");
      }
      else {
        const inicio = moment(this.inicialCtrl.value).format('YYYY-MM-DD');
        const final = moment(this.finalCtrl.value).format('YYYY-MM-DD');
        this.getParidadePorPeriodo(this.moedaCtrl.value, inicio, final)
      }
    } else if (this.moedaCtrl.value == '') {
      alert("Preencha a moeda que deseja!");
    } else {
      alert("Preencha as datas corretamente!");
    }
  }

  // Busca dados para o relatorio
  async getParidadePorPeriodo(moeda: String, inicio: String, final: String): Promise<any> {
    this.candleService.getParidadePorPeriodo(moeda, inicio, final).subscribe(
      (res) => {
        let resTempo = [];
        let resValor = [];

        for (let resposta of res){
          resTempo.push(resposta.period);
          switch (this.moedaCtrl.value) {
            case 'Real':
              resValor.push(parseFloat(resposta.real))
              break;
            case 'Euro':
              resValor.push(parseFloat(resposta.euro))
              break;
            case 'Jpy':
              resValor.push(parseFloat(resposta.jpy))
              break;
            default:
              alert("Ocorreu um erro não esperado contate o desenvolvedor!");
              break;
        }

        }
        this.chartOptions.xAxis = {categories: resTempo};
        this.chartOptions.series = [{
          data: resValor,
          type: 'line'
        }];

        this.oneToOne = true;
        this.update = true;
        this.grafico = true;

      }, error => {
        this.grafico = false;
        alert("Ocorreu um erro não esperado contate o desenvolvedor!");
      }
    );
  }

}
