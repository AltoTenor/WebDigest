import { Component } from '@angular/core';
import { PrimeNGConfig } from 'primeng/api';
import { ApiRequestService } from './Services/api-request.service';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'FOSS PROJECT';

  constructor(private primengConfig : PrimeNGConfig, private apiService : ApiRequestService) { }

  ngOnInit() {
    this.primengConfig.ripple = true;
    this.apiService.checkOnline();
  }
}
