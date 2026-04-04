import { drizzle } from 'drizzle-orm/mysql2';
import mysql from 'mysql2/promise';
import * as schema from './schema';
import { env } from '$env/dynamic/private';
import { building } from '$app/environment';

if (!building && !env.DATABASE_URL) throw new Error('DATABASE_URL is not set');

const client = building ? null : mysql.createPool(env.DATABASE_URL!);

export const db = building ? (null as any) : drizzle(client!, { schema, mode: 'default' });
