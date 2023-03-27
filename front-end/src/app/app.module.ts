import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavbarComponent } from './Components/navbar/navbar.component';
import { LogInComponent } from './Components/log-in/log-in.component';
import { SignUpComponent } from './Components/sign-up/sign-up.component';
import { HomeComponent } from './Components/home/home.component';
import { UserFormComponent } from './Components/user-form/user-form.component';
import { CardComponent } from './Components/card/card.component';

import {HttpClientModule} from '@angular/common/http';

import { FormsModule } from '@angular/forms';
import { ProfileComponent } from './Components/profile/profile.component';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    LogInComponent,
    SignUpComponent,
    HomeComponent,
    UserFormComponent,
    CardComponent,
    ProfileComponent,
   
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
