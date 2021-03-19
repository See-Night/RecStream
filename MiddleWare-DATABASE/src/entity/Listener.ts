import { Entity, Column, PrimaryColumn } from 'typeorm';

@Entity('Listener_listener')
export class Listener {

    @PrimaryColumn()
    LiveURL: string;

    @Column()
    Name: string;

    @Column()
    Platform: string;

    @Column()
    Status: number;

    @Column({ nullable: true })
    PID: string;

    @Column({ nullable: true })
    RPID: string;
    
}