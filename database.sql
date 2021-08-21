--
-- PostgreSQL database dump
--

-- Dumped from database version 13.3 (Ubuntu 13.3-1.pgdg20.04+1)
-- Dumped by pg_dump version 13.3 (Ubuntu 13.3-1.pgdg20.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: activities; Type: TABLE; Schema: public; Owner: hackbright
--

CREATE TABLE public.activities (
    activ_id integer NOT NULL,
    trip_id integer,
    activ_name character varying,
    address character varying,
    lat double precision,
    lng double precision,
    activ_date date,
    activ_time time without time zone,
    activ_note text
);


ALTER TABLE public.activities OWNER TO hackbright;

--
-- Name: activities_activ_id_seq; Type: SEQUENCE; Schema: public; Owner: hackbright
--

CREATE SEQUENCE public.activities_activ_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.activities_activ_id_seq OWNER TO hackbright;

--
-- Name: activities_activ_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hackbright
--

ALTER SEQUENCE public.activities_activ_id_seq OWNED BY public.activities.activ_id;


--
-- Name: planner; Type: TABLE; Schema: public; Owner: hackbright
--

CREATE TABLE public.planner (
    planner_id integer NOT NULL,
    user_id integer NOT NULL,
    trip_id integer NOT NULL
);


ALTER TABLE public.planner OWNER TO hackbright;

--
-- Name: planner_planner_id_seq; Type: SEQUENCE; Schema: public; Owner: hackbright
--

CREATE SEQUENCE public.planner_planner_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.planner_planner_id_seq OWNER TO hackbright;

--
-- Name: planner_planner_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hackbright
--

ALTER SEQUENCE public.planner_planner_id_seq OWNED BY public.planner.planner_id;


--
-- Name: trips; Type: TABLE; Schema: public; Owner: hackbright
--

CREATE TABLE public.trips (
    trip_id integer NOT NULL,
    trip_name character varying,
    city character varying,
    state character varying,
    zip_code integer,
    start_date date,
    end_date date,
    lat double precision,
    lng double precision
);


ALTER TABLE public.trips OWNER TO hackbright;

--
-- Name: trips_trip_id_seq; Type: SEQUENCE; Schema: public; Owner: hackbright
--

CREATE SEQUENCE public.trips_trip_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.trips_trip_id_seq OWNER TO hackbright;

--
-- Name: trips_trip_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hackbright
--

ALTER SEQUENCE public.trips_trip_id_seq OWNED BY public.trips.trip_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: hackbright
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    fname character varying,
    lname character varying,
    email character varying,
    password character varying
);


ALTER TABLE public.users OWNER TO hackbright;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: hackbright
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO hackbright;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hackbright
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: activities activ_id; Type: DEFAULT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.activities ALTER COLUMN activ_id SET DEFAULT nextval('public.activities_activ_id_seq'::regclass);


--
-- Name: planner planner_id; Type: DEFAULT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.planner ALTER COLUMN planner_id SET DEFAULT nextval('public.planner_planner_id_seq'::regclass);


--
-- Name: trips trip_id; Type: DEFAULT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.trips ALTER COLUMN trip_id SET DEFAULT nextval('public.trips_trip_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: activities; Type: TABLE DATA; Schema: public; Owner: hackbright
--

COPY public.activities (activ_id, trip_id, activ_name, address, lat, lng, activ_date, activ_time, activ_note) FROM stdin;
1	1	Dinner with Friends	5231 Wendell Lane, Sebastopol, CA, 95472	38.348009	-122.7702767	2021-12-04	17:00:00	get tipsy later
\.


--
-- Data for Name: planner; Type: TABLE DATA; Schema: public; Owner: hackbright
--

COPY public.planner (planner_id, user_id, trip_id) FROM stdin;
1	1	1
2	2	1
3	3	1
\.


--
-- Data for Name: trips; Type: TABLE DATA; Schema: public; Owner: hackbright
--

COPY public.trips (trip_id, trip_name, city, state, zip_code, start_date, end_date, lat, lng) FROM stdin;
1	Fancy	San Francisco	CA	94111	2021-12-01	2021-12-05	37.7576793	-122.5076413
34	maybe fun	San Jose	CA	95121	2021-11-05	2021-11-10	37.3361905	-121.890583
35	nail trip	Daly City	CA	95121	2021-11-05	2021-11-10	37.6904826	-122.47267
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: hackbright
--

COPY public.users (user_id, fname, lname, email, password) FROM stdin;
1	thu	hoang	thu@hoang	thuhoang
2	jackson	wang	jack@son	got7
3	sisi	hughey	si@si	hughey
34	first	last	email@email	$argon2id$v=19$m=102400,t=2,p=8$QEjJeW/t/R9DyDnnPKfUeg$/n5ipGaVr52dxgtY+MrNxA
\.


--
-- Name: activities_activ_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hackbright
--

SELECT pg_catalog.setval('public.activities_activ_id_seq', 33, true);


--
-- Name: planner_planner_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hackbright
--

SELECT pg_catalog.setval('public.planner_planner_id_seq', 33, true);


--
-- Name: trips_trip_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hackbright
--

SELECT pg_catalog.setval('public.trips_trip_id_seq', 35, true);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hackbright
--

SELECT pg_catalog.setval('public.users_user_id_seq', 34, true);


--
-- Name: activities activities_pkey; Type: CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.activities
    ADD CONSTRAINT activities_pkey PRIMARY KEY (activ_id);


--
-- Name: planner planner_pkey; Type: CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.planner
    ADD CONSTRAINT planner_pkey PRIMARY KEY (planner_id);


--
-- Name: trips trips_pkey; Type: CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.trips
    ADD CONSTRAINT trips_pkey PRIMARY KEY (trip_id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: activities activities_trip_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.activities
    ADD CONSTRAINT activities_trip_id_fkey FOREIGN KEY (trip_id) REFERENCES public.trips(trip_id);


--
-- Name: planner planner_trip_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.planner
    ADD CONSTRAINT planner_trip_id_fkey FOREIGN KEY (trip_id) REFERENCES public.trips(trip_id);


--
-- Name: planner planner_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.planner
    ADD CONSTRAINT planner_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- PostgreSQL database dump complete
--

