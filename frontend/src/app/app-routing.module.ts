import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatNativeDateModule } from '@angular/material/core';
import { MatRippleModule } from '@angular/material/core';

const routes: Routes = [];

@NgModule({
  imports: [
    RouterModule.forRoot(routes),
    MatNativeDateModule,
    MatDatepickerModule,
    MatRippleModule
  ],
  exports: [
    RouterModule,]
})
export class AppRoutingModule { }
