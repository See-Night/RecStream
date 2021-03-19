import { Entity, Column, PrimaryColumn } from 'typeorm';

@Entity('Config_config')
export class Config {

    @PrimaryColumn()
    key: string;

    @Column({ nullable: true })
    value: string;

}