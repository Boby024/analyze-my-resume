import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";
import {FormGroup} from "@angular/forms";
import {environment} from "../environments/environment.prod";
import { Dashboard, User } from '../models/user';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = `${environment.root}/account`
  headers = new HttpHeaders({ 'Content-Type': 'application/json' });

  constructor(private http: HttpClient) {}

  register(data: FormGroup): Observable<User> {
    const dataJson = data.value;
    return this.http.post<User>(`${this.apiUrl}/register`, dataJson, {headers: this.headers});
  }

  login(data: FormGroup): Observable<User> {
    const dataJson = data.value;
    console.log(dataJson);
    return this.http.post<User>(`${this.apiUrl}/login`, dataJson, { headers: this.headers });
  }

  getDashboard(): Observable<Dashboard> {
    return this.http.get<Dashboard>(`${this.apiUrl}/dashboard`);
  }
}
