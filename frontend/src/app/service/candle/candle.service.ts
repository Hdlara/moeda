import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class CandleService {

  //Instância da API
  api = environment.PYTHON_API;

  constructor(protected http: HttpClient) { }

  //Busca dados para o grafico
  getParidadePorPeriodo(moeda: String, inicio: String, final: String): Observable<any>{
    return this.http.get(`${this.api}/candle/consulta/${moeda}/${inicio}/${final}`);
  }
}
