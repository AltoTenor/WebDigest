import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
export interface apiInterface {
  question : string,
  answer ?: string,
  url ?: string,
}


@Injectable({
  providedIn: 'root'
})
export class ApiRequestService {
  private backendUrl : string = "https://Th3BossC-qnaBackend.hf.space/question";

  constructor(private http : HttpClient) { }

  sendMessage(question : string, url : string) {
    return this.http.post(this.backendUrl, { question, url });
  }

  checkOnline() {
    this.http.get('http://127.0.0.1:5000/').subscribe();
  }
}
