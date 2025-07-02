import { importProvidersFrom } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule} from "@angular/material/input";
import { MatIconModule} from "@angular/material/icon";
import {ReactiveFormsModule} from "@angular/forms";
import {MatCardModule} from "@angular/material/card";
import {NgForOf, NgIf} from "@angular/common";
import {RouterLink} from "@angular/router";
import {MatSelectModule} from '@angular/material/select';
import {MatChipGrid, MatChipsModule} from '@angular/material/chips';
import {MatTableModule} from '@angular/material/table';
import {MatSort} from "@angular/material/sort";
import {MatPaginator} from "@angular/material/paginator";
import {MatTooltipModule} from '@angular/material/tooltip';
import {MatMenuModule} from '@angular/material/menu';
import {MatDividerModule} from '@angular/material/divider'; 

export const SHARED_MATERIAL_MODULES = [
  NgIf,
  MatButtonModule,
  MatToolbarModule,
  MatFormFieldModule,
  MatInputModule,
  MatIconModule,
  ReactiveFormsModule,
  MatCardModule,
  RouterLink,
  MatSelectModule,
  NgForOf,
  MatChipsModule,
  MatChipGrid,
  MatTableModule,
  MatSort,
  MatPaginator,
  MatTooltipModule,
  MatMenuModule,
  MatDividerModule
];
