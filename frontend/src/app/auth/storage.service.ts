import { Injectable } from '@angular/core';

const USER_KEY = 'hiddensmbot-auth-user';

@Injectable({
  providedIn: 'root'
})
export class StorageService {
  private get isBrowser(): boolean {
    return typeof window !== 'undefined';
  }

  saveUser(user: any): void {
    if (this.isBrowser) {
      sessionStorage.setItem(USER_KEY, JSON.stringify(user));
    }
  }

  getUser(): any {
    if (this.isBrowser) {
      const user = sessionStorage.getItem(USER_KEY);
      return user ? JSON.parse(user) : null;
    }
    return null;
  }

  isLoggedIn(): boolean {
    return !!this.getUser();
  }

  clear(): void {
    if (this.isBrowser) {
      sessionStorage.clear();
    }
  }
}
