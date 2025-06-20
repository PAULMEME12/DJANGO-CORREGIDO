export interface User {
    id: number;
    name: string;
    email: string;
}

export interface Product {
    id: number;
    name: string;
    price: number;
}

export type OrderStatus = 'pending' | 'completed' | 'canceled';

export interface Order {
    id: number;
    userId: number;
    productId: number;
    status: OrderStatus;
    createdAt: Date;
}